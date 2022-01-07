from fastapi import APIRouter, Depends, HTTPException
from typing import List
from configs.db import get_db

from services.OrderService import OrderService
from schemas import order_schema
from configs.dependency import getUser
from configs.constant import UNPROCCESSABLE_ENTITY_ERROR
from fastapi.responses import FileResponse

class OrderController:
    router = APIRouter(prefix="/orders")


    @staticmethod
    @router.post("", dependencies=[Depends(get_db)])
    def createOrder(payload: order_schema.OrderCreation, user = Depends(getUser)):
        try:
            OrderService.createOrder(payload, user['id'])
        except Exception as e:
            if e.args[0] == UNPROCCESSABLE_ENTITY_ERROR:
                raise HTTPException(status_code=e.args[0], detail=e.args[1])
            raise e

        return {
            'data': 'success'
        }


    @staticmethod
    @router.get("", response_model=List[order_schema.OrderDetail], dependencies=[Depends(get_db)])
    def getOwnOrders(limit: int = 10, skip: int = 0, user = Depends(getUser)):
        orders = OrderService.getOwnOrders(user['id'], limit, skip)
        return orders


    @staticmethod
    @router.get("/products", response_model=List[order_schema.OrderProduct], dependencies=[Depends(get_db)])
    def getProductsOrders(limit: int = 10, skip: int = 0, user = Depends(getUser)): #user_type: int
        # user_type = 0 nếu là user, 1 nếu là store
        # truyền vào từ FE?
        
        # Store 
        #if user_type == 1:
        #    try:
        #        getOwnOrders()
        products = OrderService.getProducts(user['id'], limit, skip)
        return products

    
    @staticmethod
    @router.delete('/{id}', dependencies=[Depends(get_db)])
    def delete(id: int, user = Depends(getUser)):
        pass
        # case 1: if user want to del order -> check if user own this order
        # case 2: if store want to del order -> check if store have this order

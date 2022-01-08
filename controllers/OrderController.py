from fastapi import APIRouter, Depends, HTTPException
from typing import List
from configs.db import get_db

from services.OrderService import OrderService
from schemas import order_schema
from schemas import order_product_schema
from configs.dependency import getUser
from configs.constant import UNPROCCESSABLE_ENTITY_ERROR, NOT_FOUND_ERROR, FORBIDDEN_ERROR
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
        return OrderService.getOwnOrders(user['id'], limit, skip)


    @staticmethod
    @router.get("/products", response_model=List[order_product_schema.OrderProductDisplay], dependencies=[Depends(get_db)])
    def getProductsOrders(user_type: int, limit: int = 10, skip: int = 0, user = Depends(getUser)):
        # user_type = 1 nếu là user, 2 nếu là store
        orders = []

        # User 
        if user_type == 1:
            try:
                orders = OrderService.getOwnOrders(user['id'], limit, skip)
            except Exception as e:
                if e.args[0] == NOT_FOUND_ERROR:
                    raise HTTPException(e.args[0], detail=e.args[1])
                raise Exception(e)

        # Store
        elif user_type == 2:
            try: 
                orders = OrderService.getStoreOrders(user['id'], limit, skip)
            except Exception as e:
                if e.args[0] == NOT_FOUND_ERROR:
                    raise HTTPException(e.args[0], detail=e.args[1])
                raise Exception(e)

        return OrderService.getByListOrderID(orders, skip, limit)

    
    @staticmethod
    @router.delete('/{order_id}', dependencies=[Depends(get_db)])
    def cancelOrder(user_type: int, order_id: int, user = Depends(getUser)):
        # Cancel order
        try:
            OrderService.cancelOrder(user_type, user['id'], order_id)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(e.args[0], detail=e.args[1])
            raise Exception(e)

        return {
            "data":{
                "success": True
            }
        }

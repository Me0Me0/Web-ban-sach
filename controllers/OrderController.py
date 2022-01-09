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
            "data":{
                "success": True
            } 
        }


    @staticmethod
    @router.get("", response_model=List[order_schema.OrderDetail], dependencies=[Depends(get_db)])
    def getOwnOrders(limit: int = 10, skip: int = 0, user = Depends(getUser)):
        return OrderService.getOwnOrders(user['id'], limit, skip)


    @staticmethod
    @router.get("{order_id}", response_model=order_schema.OrderDetail, dependencies=[Depends(get_db)])
    def getDetailOrder(order_id: int, user = Depends(getUser)):
        order = OrderService.getByOrderID(order_id)
        if order.owner_id.id != user['id']:
            raise HTTPException(403, "Forbidden")
        
        return order

    
    @staticmethod
    @router.delete("/{order_id}", dependencies=[Depends(get_db)])
    def cancelOrder(order_id: int, user = Depends(getUser)):
        # Cancel order
        try:
            OrderService.cancelOrder(user['id'], order_id)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(e.args[0], detail=e.args[1])
            raise Exception(e)

        return {
            "data":{
                "success": True
            }
        }

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from configs.db import get_db

from services.OrderService import OrderService
from schemas import order_schema
from configs.dependency import getUser
from configs.constant import UNPROCCESSABLE_ENTITY_ERROR

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
    @router.get("/own", response_model=List[order_schema.OrderDetail], dependencies=[Depends(get_db)])
    def getOwnOrders(limit: int = 10, skip: int = 0, user = Depends(getUser)):
        orders = OrderService.getOwnOrders(user['id'], limit, skip)
        return orders
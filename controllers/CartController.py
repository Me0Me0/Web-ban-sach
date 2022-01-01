from fastapi import APIRouter, Depends, HTTPException
from configs.db import get_db

from services.CartService import CartService
from schemas import cart_schema
from configs.dependency import getUser
from configs.constant import DUPLICATION_ERROR

class CartController:
    router = APIRouter(prefix="/carts")

    @staticmethod
    @router.post("", dependencies=[Depends(get_db)])
    def createCart(user = Depends(getUser)):
        CartService.createCart(user['id'])
        
        return {
            'data': 'success'
        }
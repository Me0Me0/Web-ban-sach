from fastapi import APIRouter, HTTPException
#from configs.db import get_db
import configs
from fastapi.params import Depends, Query

from configs.constant import NOT_FOUND_ERROR, DUPLICATION_ERROR, FORBIDDEN_ERROR
from services.CartService import CartService
from schemas import cart_schema
from configs.dependency import getUser
from configs.constant import DUPLICATION_ERROR
from fastapi.responses import FileResponse

class CartController:
    router = APIRouter(prefix='/cart')

    @staticmethod
    @router.post('', dependencies=[Depends(configs.db.get_db)])
    def createCart(user = Depends(getUser)):
        try:
            cart_id = CartService.createCart(user['id'])
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == DUPLICATION_ERROR:
                raise HTTPException(status_code=e.args[0], detail=e.args[1])
            raise Exception(e)

        return {
            'id': cart_id
        }

    @staticmethod
    @router.get('', dependencies=[Depends(configs.db.get_db)])
    def cartDetail(user = Depends(getUser)):
        try:
            cart_id = CartService.getOwnCart(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        
        products = CartService.getAll(cart_id)
        
        return products
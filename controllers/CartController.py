from fastapi import APIRouter, HTTPException
#from configs.db import get_db
import configs
from fastapi.params import Depends, Query

from services.CartService import CartService
from schemas import cart_schema
from configs.dependency import getUser
from configs.constant import DUPLICATION_ERROR
from fastapi.responses import FileResponse

class CartController:
    router = APIRouter(prefix="/carts")

    # @staticmethod
    # @router.post("", dependencies=[Depends(get_db)])
    # def createCart(user = Depends(getUser)):
    #     CartService.createCart(user['id'])
        
    #     return {
    #         'data': 'success'
    #     }

    @staticmethod
    @router.get('', response_class=FileResponse,dependencies=[Depends(configs.db.get_db)])
    def getCart():
        return "./views/cart/index.html"
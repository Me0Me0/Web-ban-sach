from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
import configs
from configs.constant import FORBIDDEN_ERROR

from configs.dependency import getUser
from services.ProductService import ProductService


class ProductController:
    router = APIRouter(prefix='/products')

    @staticmethod
    @router.delete('/{id}', dependencies=[Depends(configs.db.get_db)])
    def delete(id: int, user = Depends(getUser)):
        try:
            ProductService.delete(id, user['id'])
        except Exception as e:
            if e.args[0] == 'NOT_FOUND' or e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(status_code=e.args[0], detail=e.args[1])
            raise Exception(e)
            
        return {
            "data": {
                "success": True
            }
        }
        
from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.responses import Response
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR, FORBIDDEN_ERROR
from schemas import product_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from configs.dependency import getUser

from services.ProductService import ProductService

class ProductController:
    router = APIRouter(prefix='/products')

    @staticmethod
    @router.get('/{id}',response_model=product_schema.Product,dependencies=[Depends(configs.db.get_db)])
    def getById(id: int):
        product = ProductService.getById(id)
        if not product:
            raise HTTPException(404, detail="Product not found!")
        return product
      
      
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
    
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.responses import Response
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR
#from configs.dependency import getProduct
from schemas import product_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.ProductService import ProductService

class ProductController:
    router = APIRouter(prefix='/product')


    @staticmethod
    @router.get('/{id}',response_model=product_schema.Product,dependencies=[Depends(configs.db.get_db)])
    def getByID(id: int):
        product = ProductService.getById(id)
        if not product:
            raise HTTPException(404, detail="Product not found!")
        return product

    
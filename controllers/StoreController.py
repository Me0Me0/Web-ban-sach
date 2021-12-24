from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.responses import Response
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR
from configs.dependency import getStore
from schemas import store_schema
from schemas import product_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.StoreService import StoreService
from services.ProductService import ProductService

class StoreController:
    router = APIRouter(prefix='/store')


    # Dang san pham
    @staticmethod
    @router.post('/product/new', dependencies=[Depends(configs.db.get_db)])
    def createProduct(payload: product_schema.ProductCreate, currentStore = Depends(getStore)):
        try:
            id = StoreService.createProduct(payload, 1)#currentStore['id'])
        except Exception as e:
            if e.args[0] == DUPLICATION_ERROR:
                raise HTTPException(409, detial=e.args[1])
            raise Exception(e)
        return {
            "data":{
                "id":id
            }
        }
    

    # Quan ly san pham
    @staticmethod
    @router.get('', dependencies=[Depends(configs.db.get_db)])
    def getAll(currentStore = Depends(getStore)):
        limit = Query(10, gt=0)
        skip = Query(0, ge=0)
        return StoreService.getAll(skip, limit, currentStore['id'])

    
    # Dieu chinh san pham
    @staticmethod
    @router.put('/product/{product_id}', dependencies=[Depends(configs.db.get_db)])
    def update(product_id: int, payload: product_schema.ProductUpdate, currentStore = Depends(getStore)):
        try:
            ProductService.update(product_id, payload)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(404, detail=e.args[1])
            raise Exception(e)
        
        return {
            "data": {
                "success": True
            }
        }
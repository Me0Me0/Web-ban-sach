from typing import List
from fastapi import APIRouter
<<<<<<< Updated upstream
from fastapi.params import Depends, Query
=======
from fastapi.exceptions import HTTPException
from fastapi.params import Depends, Query
from starlette.responses import FileResponse
#from fastapi.responses import FileResponse
>>>>>>> Stashed changes
from fastapi.responses import Response
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR
from configs.dependency import getStore
from schemas import store_schema
from schemas import product_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.StoreService import StoreService
<<<<<<< Updated upstream
from services.ProductService import ProductService

class StoreController:
    router = APIRouter(prefix='/store')
=======
from schemas import store_schema
from schemas import product_schema
from services.ProductService import ProductService

class StoreController:
    router = APIRouter(prefix='/stores')

    # Handle store operations from owner
    router2 = APIRouter(prefix='/mystore')

    # -----------------------------------------------------------------------------
    # Mystore - View nguoi ban


    #@staticmethod
    #@router2.get('', response_class=FileResponse)
    #def mystore_page():
    #    pass # UI page


    @staticmethod
    @router2.get('', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def getAll(user = Depends(getUser)):
        """Return: 
           [store_info_dict, list(product_info_dict)]"""
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        limit = Query(10, gt=0)
        skip = Query(0, ge=0)
        return StoreService.getAll(skip, limit, store['id'])
>>>>>>> Stashed changes


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
<<<<<<< Updated upstream
            "data": {
                "success": True
            }
        }
=======
            "id": store_id
        }

        
    @staticmethod
    @router2.post('/products/new', dependencies=[Depends(configs.db.get_db)])
    def createProduct(payload: product_schema.ProductCreate, user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
            
        # Create product
        try:
            id = StoreService.createProduct(payload, store['id'])
        except Exception as e:
            if e.args[0] == DUPLICATION_ERROR:
                raise HTTPException(409, detail=e.args[1])
            raise Exception(e)

        return {
            "data":{
                "id":id
            }
        }
        
    # Dieu chinh san pham
    @staticmethod
    @router2.put('/products/{product_id}', dependencies=[Depends(configs.db.get_db)])
    def updateProduct(product_id: int, payload: product_schema.ProductUpdate, user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)

        try:
            ProductService.update(store, product_id, payload)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(404, detail=e.args[1])
            raise Exception(e)
        
        return {
            "data": {
                "success": True
            }
        }


    # -----------------------------------------------------------------------------
    # Store - View nguoi dung
    
    @staticmethod
    @router.get('/{store_id}', dependencies=[Depends(configs.db.get_db)])
    def getAll(store_id: int):
        limit = Query(10, gt=0)
        skip = Query(0, ge=0)
        return StoreService.getAll(skip, limit, store_id)
>>>>>>> Stashed changes

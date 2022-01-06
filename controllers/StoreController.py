from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends, Query
from starlette.responses import FileResponse
from fastapi.responses import Response
import configs

from configs.constant import NOT_FOUND_ERROR, DUPLICATION_ERROR, FORBIDDEN_ERROR
from configs.dependency import getUser
from schemas import store_schema
from schemas import product_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.StoreService import StoreService
from schemas import store_schema
from schemas import product_schema
from services.ProductService import ProductService

class StoreController:
    router = APIRouter(prefix='/stores')

    
    # Handle store operations from owner
    router2 = APIRouter(prefix='/mystore')


    # -----------------------------------------------------------------------------
    # Mystore - View nguoi ban

    
    @staticmethod
    @router2.get('', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def mystore_page():
        return "./views/storeViewSeller/index.html"

    @staticmethod
    @router2.get('/add-product', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def mystore_page():
        return "./views/addProduct/index.html"

    @staticmethod
    @router2.get('/register', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def mystoreRegistration():
        return "./views/stroreRegistration/index.html"

    @staticmethod
    @router2.get('/details', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def mystoreDetails():
        return "./views/storeDetails_ViewSeller/index.html"

    @staticmethod
    @router2.get('/edit', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def mystoreEdit():
        return "./views/editStore/index.html"

      
    @staticmethod
    @router2.post('/register')
    def registerStore(user = Depends(getUser)):
        try:
            store_id = StoreService.registerStore(user['id'])
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == DUPLICATION_ERROR:
                raise HTTPException(status_code=e.args[0], detail=e.args[1])
            raise Exception(e)

        return {
            "id": store_id
        }  
     

    @staticmethod
    @router2.get('/details', dependencies=[Depends(configs.db.get_db)])
    def storeDetail(user = Depends(getUser)):
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
                raise HTTPException(status_code=409, detail=e.args[1])
            raise Exception(e)

        return {
            'data':'success'
        }
        
        
    @staticmethod
    @router2.put('/products/{product_id}', dependencies=[Depends(configs.db.get_db)])
    def updateProduct(product_id: int, payload: product_schema.ProductUpdate, user = Depends(getUser)):
        try:
            ProductService.update(store['id'], product_id, payload)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(status_code=404, detail=e.args[1])
            elif e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(status_code=403, detail=e.args[1])
            raise Exception(e) 
        
        return {
            "data": {
                "success": True
            }
        }


    # -----------------------------------------------------------------------------
    # Store - View nguoi dung

    @staticmethod
    @router.get('/{store_id}', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def storePage():
        return "./views/storeViewCus/index.html"

    @staticmethod
    @router.get('/{store_id}/details', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
    def mystoreDetails():
        return "./views/storeDetails_ViewCus/index.html"
    
    @staticmethod
    @router.get('/{store_id}', dependencies=[Depends(configs.db.get_db)])
    def getAll(store_id: int):
        limit = Query(10, gt=0)
        skip = Query(0, ge=0)
        return StoreService.getAll(skip, limit, store_id)

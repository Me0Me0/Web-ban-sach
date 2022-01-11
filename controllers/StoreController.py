from fastapi import APIRouter
from typing import List
from fastapi.exceptions import HTTPException
from fastapi.params import Depends, Query
from starlette.responses import FileResponse
from fastapi.responses import Response
import configs

from configs.constant import NOT_FOUND_ERROR, DUPLICATION_ERROR, FORBIDDEN_ERROR
from configs.dependency import getUser
from schemas import store_schema
from schemas import product_schema
from schemas import order_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.StoreService import StoreService
from services.OrderService import OrderService
from services.ProductService import ProductService

class StoreController:
    router = APIRouter(prefix='/stores')

    
    # Handle store operations from owner
    router2 = APIRouter(prefix='/mystore')


    # -----------------------------------------------------------------------------
    # Mystore - View nguoi ban
      
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
    @router2.get('', dependencies=[Depends(configs.db.get_db)])
    def getStoreDetail(user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        return StoreService.getStoreDetail(store['id'])


    @staticmethod
    @router2.put('/details', dependencies=[Depends(configs.db.get_db)])
    def update(payload: store_schema.StoreUpdate, currentUser = Depends(getUser)):
        try:
            StoreService.update(currentUser['id'], payload)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == 409:
                raise HTTPException(e.args[0], detail=e.args[1])
            raise Exception(e)
            
        return {
            "data": {
                "success": True
            }
        }
       
    
    @staticmethod
    @router2.get('/products', dependencies=[Depends(configs.db.get_db)])
    def getStoreProduct(limit:int = Query(10, gt=0), skip:int = Query(0, ge=0), user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        
        products = StoreService.getStoreProduct(skip, limit, store['id'])
        
        return products


    @staticmethod
    @router2.post('/products/new', dependencies=[Depends(configs.db.get_db)])
    def createProduct(payload: product_schema.ProductCreate, user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
            product_id = StoreService.createProduct(payload, store['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)

        return {
            "id": product_id
        }
        
        
    @staticmethod
    @router2.put('/products/{product_id}', dependencies=[Depends(configs.db.get_db)])
    def updateProduct(product_id: int, payload: product_schema.ProductUpdate, user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)

        try:
            ProductService.update(store['id'], product_id, payload)
        except Exception as e:
            if e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(status_code=403, detail=e.args[1])
            raise Exception(e) 
        
        return {
            "data": {
                "success": True
            }
        }


    @staticmethod
    @router2.put('/products/{product_id}/cover-images', dependencies=[Depends(configs.db.get_db)])
    def updateProductCoverImage(product_id: int, payload: product_schema.ProductUpdateCoverImage, user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)

        try:
            ProductService.updateCoverImage(store['id'], product_id, payload.image_link)
        except Exception as e:
            if e.args[0] == FORBIDDEN_ERROR or e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(status_code=e.args[0], detail=e.args[1])
            raise Exception(e)
        
        return {
            "data":{
                "success": True
            }
        }

    
    @staticmethod
    @router2.post('/products/{product_id}/images', dependencies=[Depends(configs.db.get_db)])
    def updateProductImage(product_id: int, payload: product_schema.ProductUpdateImages, user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)

        try:
            ProductService.updateImage(store['id'], product_id, payload.list_image_link)
        except Exception as e:
            if e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(status_code=403, detail=e.args[1])
            raise Exception(e)

        return {
            "data":{
                "success": True
            }
        }
    

    @staticmethod
    @router2.get('/orders', response_model=List[order_schema.OrderDetail], dependencies=[Depends(configs.db.get_db)])
    def getStoreOrders(limit: int = 10, skip: int = 0, user = Depends(getUser)):
        return OrderService.getStoreOrders(user['id'], limit, skip)


    @staticmethod
    @router2.get('/orders/{order_id}', response_model=order_schema.OrderDetail, dependencies=[Depends(configs.db.get_db)])
    def getDetailOrder(order_id: int, user = Depends(getUser)):
        order = OrderService.getByOrderID(order_id)
        store = StoreService.getOwnStore(user['id'])

        if order.store_id.id != store['id']:
            raise HTTPException(403, "Forbidden")
        
        return order


    @staticmethod
    @router2.delete('/orders/{order_id}', dependencies=[Depends(configs.db.get_db)])
    def cancelOrder(order_id: int, user = Depends(getUser)):
        try:
            StoreService.cancelOrder(user['id'], order_id)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(e.args[0], detail=e.args[1])
            raise Exception(e)
        
        return {
            "data":{
                "success": True
            }
        }


    # Thống kê kinh doanh của store:
    # Thể loại bán nhiều nhất; Sách bán nhiều nhất; Tổng giao dịch 
    @staticmethod
    @router2.get('/business/best-sell-categories', response_model=List[product_schema.ProductBestSellCate], dependencies=[Depends(configs.db.get_db)])
    def getBestSellCate(user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        
        return StoreService.getBestSellCate(store['id'])
        

    @staticmethod
    @router2.get('/business/best-sell-products', response_model=List[product_schema.ProductBestSell], dependencies=[Depends(configs.db.get_db)])
    def getBestSellProducts(user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        
        return StoreService.getBestSellProducts(store['id'])
    

    @staticmethod
    @router2.get('/business/total-income', dependencies=[Depends(configs.db.get_db)])
    def getTotalIncome(user = Depends(getUser)):
        # Store id
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        
        totalIncome = StoreService.getTotalIncome(store['id'])

        return {
            "data":{
                "total-income": totalIncome
            }
        }

    # -----------------------------------------------------------------------------
    # Store - View nguoi dung
    
    @staticmethod
    @router.get('/{store_id}/products', dependencies=[Depends(configs.db.get_db)])
    def getProducts(store_id: int, skip: int = 0, limit: int = 10):
        products = StoreService.getStoreProduct(skip, limit, store_id)
        return products

    
    @staticmethod
    @router.get('/{store_id}',dependencies=[Depends(configs.db.get_db)])
    def getDetail(store_id: int):
        return StoreService.getStoreDetail(store_id)


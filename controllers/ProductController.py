from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.responses import Response
from typing import Optional
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR, FORBIDDEN_ERROR
from schemas import product_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from configs.dependency import getUser
from repositories import CartProductRepository
from repositories import CartRepository
from services.ProductService import ProductService
from services.CartService import CartService

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
    

    # Them san pham vao gio hang
    @staticmethod
    @router.post('/{product_id}/add-to-cart', dependencies=[Depends(configs.db.get_db)])
    def addToCart(product_id: int, user = Depends(getUser)):
        try:
            cart_id = CartService.getCartID(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
            
        ProductService.addToCart(cart_id, product_id, 1)  # Số lượng ban đầu là 1

        return {
            "data": {
                "success": True
            }
        }

    
    # DS san pham moi nhat
    @staticmethod
    @router.post('/newest', dependencies=[Depends(configs.db.get_db)])
    def getProductNew(limit:int = Query(10, gt=0), skip:int = Query(0, ge=0)):
        return ProductService.getProductNew(True, skip, limit)


    # DS san pham ban chay nhat
    @staticmethod
    @router.post('/top-product', dependencies=[Depends(configs.db.get_db)])
    def getTopProduct(limit:int = Query(10, gt=0), skip:int = Query(0, ge=0)):
        return ProductService.getTopProduct(True, skip, limit)


    # Hien thi san pham theo doanh muc
    @staticmethod
    @router.post('/category', dependencies=[Depends(configs.db.get_db)])
    def getProductByCategory(cate_id: int, limit:int = Query(10, gt=0), skip:int = Query(0, ge=0)):
        return ProductService.getProductByCategory(cate_id, skip, limit)


    # Search
    @staticmethod
    @router.post('/search', dependencies=[Depends(configs.db.get_db)])
    def searchProduct(keyword:str, category: Optional[int]=None, maxPrice: Optional[int]=None, minPrice: Optional[int]=None, order: Optional[str]='asc', sortBy: Optional[str]=None):
        return ProductService.searchProduct(keyword, category, maxPrice, minPrice, order, sortBy)
    
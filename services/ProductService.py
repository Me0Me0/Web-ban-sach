from datetime import datetime
from repositories.ProductRepository import ProductRepository
from repositories.StoreRepository import StoreRepository
from repositories.CategoryRepository import CategoryRepository
from repositories.CartProductRepository import CartProductRepository
from fastapi.exceptions import HTTPException
from schemas import product_schema
from configs.constant import DEFAULT_AVT


class ProductService:

    @classmethod
    def getById(cls, id):
        return ProductRepository.getById(id)

      
    @classmethod
    def delete(cls, id, user_id):
        stores = StoreRepository.getByUserId(user_id)
        product = ProductRepository.getById(id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")

        ProductRepository.deleteById(id)
        

    @classmethod
    def update(cls, user_id, product_id, payload):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) ==0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")

        return ProductRepository.update(product_id, payload.__dict__)

    
    @classmethod
    def addToCart(cls, cart_id, product_id, quantity):
        return CartProductRepository.create(cart_id, product_id, quantity)


    @classmethod
    def getProductNew(cls, ascending, skip, limit):
        return ProductRepository.getSortByDate(ascending, skip, limit)


    @classmethod
    def getTopProduct(cls, ascending, skip, limit):
        return ProductRepository.getSortBySell(ascending, skip, limit)


    @classmethod
    def getProductByName(cls, name):
        return ProductRepository.getByName(name)


    @classmethod
    def getProductFromCategory(cate_id):
        category = CategoryRepository.getById(cate_id)
        if not category:
            raise HTTPException(status_code=404, detail="")
        return ProductRepository.getProductFromCategory(cate_id)

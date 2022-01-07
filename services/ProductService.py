from datetime import datetime
from repositories.ProductRepository import ProductRepository
from repositories.ProductImageRepository import ProductImageRepository
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

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")

        return ProductRepository.update(product_id, payload.__dict__)


    @classmethod
    def updateCoverImage(cls, user_id, product_id, image_link):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")
        
        return ProductRepository.updateImage(product_id, image_link)
        
    
    @classmethod
    def updateImage(cls, user_id, product_id, list_image_link):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")
        
        image_list = []
        for image_link in range(len(list_image_link)):
            image_list.append((product_id, image_link))
        
        return ProductImageRepository.createMany(image_list)
        
    
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
    def getProductByCategory(cls, cate_id, skip, limit):
        category = CategoryRepository.getById(cate_id)
        if not category:
            raise HTTPException(status_code=404, detail="")
        return ProductRepository.getByCate(cate_id, skip, limit)

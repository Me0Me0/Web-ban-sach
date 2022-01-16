from datetime import datetime
from tkinter import Image
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
            raise Exception(403, "Forbidden")

        # Các order có sản phẩm này và đang trong status 1 hoặc 2
        productsOnOrder = ProductRepository.inOrderWithStatus(id)
        if len(productsOnOrder) > 0:
            raise Exception(403, "Can't delete, products are currently on order")
        
        ProductRepository.deleteById(id)
        

    @classmethod
    def update(cls, user_id, product_id, payload):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0:
            raise Exception(404, "Not found store")

        if product.store_id.id != stores[0].id:
            raise Exception(403, "Forbidden")

        return ProductRepository.update(product_id, payload.__dict__)


    @classmethod
    def updateCoverImage(cls, user_id, product_id, image_link):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0:
            raise Exception(404, "Not found store") 
        
        if product.store_id.id != stores[0].id:
            raise Exception(403, "Forbidden")
        
        return ProductRepository.updateImage(product_id, image_link)
        
    
    @classmethod
    def updateImage(cls, user_id, product_id, list_image_link):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0:
            raise Exception(404, "Not found store")
        
        if product.store_id != stores[0]:
            raise Exception(403, "Forbidden")
        
        for image in list_image_link:
            if image.id == -1:
                ProductImageRepository.create(product_id, image.image_link)
            else:
                ProductImageRepository.updateImage(image.id, image.image_link)
        
    
    @classmethod
    def addToCart(cls, cart_id, product_id, quantity):
        product_quantity = ProductRepository.getById(product_id).quantity
        if product_quantity < quantity:
            raise Exception(422, "Unprocessable Entity")

        return CartProductRepository.create(cart_id, product_id, quantity)


    @classmethod
    def getProductNew(cls, ascending, skip, limit):
        return ProductRepository.getSortByDate(ascending, skip, limit)


    @classmethod
    def getTopProduct(cls, ascending, skip, limit):
        return ProductRepository.getSortBySell(ascending, 3, skip, limit)


    @classmethod
    def getTopCategory(cls, skip, limit):
        return ProductRepository.getTopCate(3, skip, limit)


    @classmethod
    def getProductByName(cls, name):
        return ProductRepository.getByName(name)


    @classmethod
    def getListCategory(cls):
        return CategoryRepository.getAll()


    @classmethod
    def getCategoryByID(cls, id: int):
        return CategoryRepository.getById(id)


    @classmethod
    def getProductByCategory(cls, cate_id, skip, limit):
        category = CategoryRepository.getById(cate_id)
        if not category:
            raise HTTPException(status_code=404, detail="")
        return ProductRepository.getByCate(cate_id, skip, limit)


    @classmethod
    def searchProduct(cls, keyword, field, ascending, skip, limit):
        try:
            products_rslt = ProductRepository.searchByName(keyword, field, ascending, skip, limit)
            return products_rslt
        except:
            raise Exception(422, "Unprocessable entity")
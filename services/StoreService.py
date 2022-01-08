from fastapi import APIRouter
from repositories.StoreRepository import StoreRepository
from repositories.UserRepository import UserRepository
from repositories.ProductRepository import ProductRepository
from schemas import store_schema
from schemas import product_schema
from configs.constant import DEFAULT_AVT

class StoreService:

    @classmethod
    def getOwnStore(cls, user_id):
        stores = StoreRepository.getByUserId(user_id)
        if len(stores) == 0:
            raise Exception(404, "not found")
        return stores[0].__data__


    @classmethod
    def registerStore(cls, user_id):
        user = UserRepository.getById(user_id)
        if not user: 
            raise Exception(404, "not found")

        stores = StoreRepository.getByUserId(user_id)
        if len(stores) > 0:
            raise Exception(409, "already exists")

        store = {
            "name": user.username,
            "owner_id": user.id,
            "phone": user.phone,
            "email": user.email,
            "rating": 0,
            "description": ""
        }
        return StoreRepository.create(store)


    @classmethod
    def createProduct(cls, payload: product_schema.ProductCreate, store_id):
        productDict = payload.__dict__
        productDict['avt_link'] = DEFAULT_AVT
        # Get category of product
        category = productDict['cate_id']
        # Remove category field from productDict 
        del productDict['cate_id']
        return ProductRepository.create(store_id, category, productDict)

    
    @classmethod
    def getStoreDetail(cls, store_id):
        return StoreRepository.getById(store_id)

    
    @classmethod
    def getStoreProduct(cls, skip, limit, store_id):
        return ProductRepository.getByStore(store_id, skip, limit)


    @classmethod
    def getBestSellCate(cls, store_id):
        return ProductRepository.getBestSellByCate(store_id)

    
    @classmethod
    def getBestSellProducts(cls, store_id):
        return ProductRepository.getBestSellByStore(store_id)


    @classmethod
    def getTotalIncome(cls, store_id):
        return StoreRepository.getTotalIncome(store_id)
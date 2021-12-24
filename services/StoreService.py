from datetime import datetime
from repositories.StoreRepository import StoreRepository
from repositories.ProductRepository import ProductRepository
from schemas import store_schema
from schemas import product_schema
from configs.constant import DEFAULT_AVT


class StoreService:

    @classmethod
    def createProduct(cls, payload: product_schema.ProductCreate, store_id):
        productDict = payload.__dict__
        productDict['avt_link'] = DEFAULT_AVT
        return ProductRepository.create(store_id, payload.__dict__) 

    @classmethod
    def getAll(cls, skip, limit, store_id):
        return [StoreRepository.getById(store_id), ProductRepository.getByStore(store_id)]
    

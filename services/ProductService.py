from datetime import datetime
from repositories.ProductRepository import ProductRepository
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
    def update(cls, store_id, product_id, payload):
        return ProductRepository.update(store_id, product_id, payload.__dict__)

            
            

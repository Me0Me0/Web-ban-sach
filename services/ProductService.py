from datetime import datetime
from repositories.ProductRepository import ProductRepository
from repositories.StoreRepository import StoreRepository
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
    def update(cls, store_id, product_id, payload):
        # Check if this product_id owned by store_id
        #try:
        #    product = ProductRepository.getById(product_id)
        #except Exception as e:
        #    raise Exception(e)
        
        #if product["store_id"] != store_id:
        #    raise HTTPException(status_code=403, detail="forbidden")
        return ProductRepository.update(product_id, payload.__dict__)

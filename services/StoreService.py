from datetime import datetime
from repositories.StoreRepository import StoreRepository
<<<<<<< Updated upstream
=======
from repositories.UserRepository import UserRepository
>>>>>>> Stashed changes
from repositories.ProductRepository import ProductRepository
from schemas import store_schema
from schemas import product_schema
from configs.constant import DEFAULT_AVT
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

class StoreService:

    @classmethod
    def createProduct(cls, payload: product_schema.ProductCreate, store_id):
        productDict = payload.__dict__
        productDict['avt_link'] = DEFAULT_AVT
        return ProductRepository.create(store_id, payload.__dict__) 

    @classmethod
<<<<<<< Updated upstream
    def getAll(cls, skip, limit, store_id):
        return [StoreRepository.getById(store_id), ProductRepository.getByStore(store_id)]
    
=======
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
        category = productDict['category']
        # Remove category field from productDict 
        del productDict['category']
        return ProductRepository.create(store_id, category, productDict)

    
    @classmethod
    def getAll(cls, skip, limit, store_id):
        return [StoreRepository.getById(store_id), ProductRepository.getByStore(store_id, skip, limit)]
>>>>>>> Stashed changes

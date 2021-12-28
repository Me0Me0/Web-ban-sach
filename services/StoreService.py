from fastapi import APIRouter
from repositories.StoreRepository import StoreRepository
from repositories.UserRepository import UserRepository

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
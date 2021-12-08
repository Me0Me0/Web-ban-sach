from peewee import *
from models.Store import Store
from models.User import User


class StoreRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Store.select().offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):
      return Store.get_by_id(id)


   @classmethod
   def getByUserId(cls, user_id: int):
      return list(Store.select().where(Store.owner_id == user_id))


   @classmethod
   def create(cls, storeDict):
       return Store.create(**storeDict).id


   #return -1 if user already has a store
   #return store's id if success
   @classmethod
   def createByUserId(cls, user_id, storeDict):
       try:
           user = User.get_by_id(user_id)
       except:
           raise Exception(404, { "Store - createByUserId ERROR": "Can not find user with given id" })

       # Each user only has one store, return -1 if user already has a store
       num = len(list(Store.select().join(User).where(Store.owner_id == user_id)))
       if num > 0:
           return -1

       return Store.create(owner_id = user_id, **storeDict).id



   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_store = Store.get_by_id(id)
      except:
         raise Exception(404, { "DELETE ERROR": "Can not find store with given id" })

      return delete_store.delete_instance()
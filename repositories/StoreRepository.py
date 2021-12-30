from peewee import *
from peewee import datetime
from datetime import timedelta
from models.Store import Store
from models.User import User
from repositories.ProductRepository import ProductRepository


class StoreRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Store.select().offset(skip).limit(limit))


   @classmethod
   def getDeletedStore(cls, skip: int = 0, limit: int = 100):
      return list(Store.select().where(Store.deleted_at.is_null(False)).offset(skip).limit(limit))


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
           raise Exception("Can not find user with given id")

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
         raise Exception("Can not find store with given id")


      if (delete_store.deleted_at != None):
         return 0

      delete_store.deleted_at = datetime.datetime.now().date()

      return delete_store.save()


   @classmethod
   def deleteByUserId(cls, id: int):
      try:
         delete_store = Store.get(Store.owner_id == id)
      except DoesNotExist:
         return 0

      if (delete_store.deleted_at != None):
         return 0

      delete_store.deleted_at = datetime.datetime.now().date()
      ProductRepository.deleteByStoreId(delete_store.id)
      
      return delete_store.save()


   # Delete from DB, only Admin use this method
   @classmethod
   def deleteFromDB(cls, max_day: int = 30):
      ProductRepository.deleteFromDB()
      query = Store.delete().where(Store.deleted_at <= datetime.datetime.now().date() - timedelta(days=max_day))

      return query.execute()
from peewee import *
from peewee import datetime
from datetime import timedelta
from models.Store import Store
from models.User import User
from models.OrderDetail import OrderDetail
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
   def getTotalIncome(cls, store_id: int, status: int = 3):
      query = Store.select(fn.SUM(OrderDetail.total_cost).alias('sum')).join(OrderDetail, JOIN.LEFT_OUTER).where((OrderDetail.status == status) & (Store.id == store_id)).group_by(Store.id).order_by(fn.SUM(OrderDetail.total_cost).desc())
      total = 0.0
      for i in query:
         total = i.sum

      return total


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
   def updateByUserID(cls, user_id: int, storeDict):
      try:
         update_store = Store.get(Store.owner_id == user_id)
      except:
         raise Exception("Can not find store with given user id")

      update_store.name = storeDict["name"]
      update_store.phone = storeDict["phone"]
      update_store.email = storeDict["email"]
      update_store.description = storeDict["description"]
      
      return update_store.save()


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
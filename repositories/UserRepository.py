from peewee import *
from peewee import datetime
from datetime import timedelta
from models.User import User
from repositories.StoreRepository import StoreRepository


class UserRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(User.select().offset(skip).limit(limit))


   @classmethod
   def getDeletedUser(cls, skip: int = 0, limit: int = 100):
      return list(User.select().where(User.deleted_at.is_null(False)).offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):
      result = None
      for record in User.select().where(User.id == id & User.deleted_at.is_null(True)):
         result = record

      return result
   

   @classmethod
   def getByUsername(cls,username) -> str:
      result = None
      for record in User.select().where(User.username==username & User.deleted_at.is_null(True)):
         result = record

      return result

   
   @classmethod
   def getByEmail(cls,email) -> str:
      result = None
      for record in User.select().where(User.email==email):
         result = record

      return result


   @classmethod
   def create(cls, userDict):
      try:
         return User.create(**userDict).id
      except Exception as e:
         if e.args[0] == 1062:
            field = "email"
            if "user.username" in e.args[1]:
               field = "username"
            raise Exception(409, { "field": field })


   # update delete date
   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_user = User.get_by_id(id)
      except:
         raise Exception(404, {"Can not find user with given id" })

      if (delete_user.deleted_at != None):
         return 0

      delete_user.deleted_at = datetime.datetime.now().date()
      StoreRepository.deleteByUserId(delete_user.id)

      return delete_user.save()


   # Delete from DB, only Admin use this method
   @classmethod
   def deleteFromDB(cls, max_day: int = 30):
      StoreRepository.deleteFromDB()
      query = User.delete().where(User.deleted_at <= datetime.datetime.now().date() - timedelta(days=max_day))

      return query.execute()



   @classmethod
   def updatePassword(cls, id: int, passwd: str):
      try:
         update_user = User.get_by_id(id)
      except:
         raise Exception(404, {"Can not find user with given id" })

      update_user.password = passwd
      return update_user.save()


   @classmethod
   def update(cls, id: int, userDict):
      try:
         update_user = User.get_by_id(id)
      except:
         raise Exception(404, {"Can not find user with given id" })

      update_user.name = userDict["name"]
      update_user.email = userDict["email"]
      update_user.dob = userDict["dob"]
      update_user.phone = userDict["phone"]
      
      return update_user.save()


   # @classmethod
   # def updatePhone(cls, id: int, number: int):
   #    try:
   #       update_user = User.get_by_id(id)
   #    except:
   #       raise Exception(404, { "UPDATE ERROR": "Can not find user with given id" })

   #    update_user.phone = number
   #    return update_user.save()


   # @classmethod
   # def updateAvatar(cls, id: int, link: str):
   #    try:
   #       update_user = User.get_by_id(id)
   #    except:
   #       raise Exception(404, { "UPDATE ERROR": "Can not find user with given id" })

   #    update_user.avt_link = link
   #    return update_user.save()

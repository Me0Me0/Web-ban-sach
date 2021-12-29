from peewee import *
from models.Admin import Admin

class AdminRepository():


   @classmethod
   def getById(cls, id: int):
      return list(Admin.select().where(Admin.id == id))

   
   @classmethod
   def create(cls, adminDict):
       return Admin.create(**adminDict).id


   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_admin = Admin.get_by_id(id)
      except:
         raise Exception(404, {"Can not find admin with given id" })

      return delete_admin.delete_instance()
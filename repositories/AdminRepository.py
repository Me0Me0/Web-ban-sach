from peewee import *
from playhouse.shortcuts import model_to_dict
from models.Admin import Admin

class AdminRepository():


   @classmethod
   def getById(cls, id: int):
      query = Admin.select().where(Admin.id == id).get()
      return model_to_dict(query)


   @classmethod
   def getByName(cls, name: str):
      try:
         query = Admin.select().where(Admin.username == name).get()
         return model_to_dict(query)
      except:
         return None

   
   @classmethod
   def create(cls, adminDict):
       return Admin.create(**adminDict).id


   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_admin = Admin.get_by_id(id)
      except:
         raise Exception("Can not find admin with given id")

      return delete_admin.delete_instance()
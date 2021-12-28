from peewee import *
from models.Ward import Ward

class WardRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Ward.select().offset(skip).limit(limit))


   @classmethod
   def getByID(cls, id: int):
       try:
           return Ward.get_by_id(id)
       except:
           raise Exception("Does not exist ward with given id")


   @classmethod
   def getIDByName(cls, name: str):
       try:
           return Ward.get(Ward._name == name)
       except:
           raise Exception("Does not exist ward with given name")


   @classmethod
   def getByDistrict(cls, district_id: int):
       query = Ward.select().where(Ward._district_id == district_id).dicts()
       return list(query.execute())   
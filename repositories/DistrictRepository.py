from peewee import *
from models.District import District

class DistrictRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(District.select().offset(skip).limit(limit))


   @classmethod
   def getByID(cls, id: int):
       try:
           return District.get_by_id(id)
       except:
           raise Exception("Does not exist district with given id")


   @classmethod
   def getIDByName(cls, name: str):
       try:
           return District.get(District._name == name)
       except:
           raise Exception("Does not exist district with given name")


   @classmethod
   def getByProvince(cls, province_id: int):
       query = District.select().where(District._province_id == province_id).dicts()
       return list(query.execute())   
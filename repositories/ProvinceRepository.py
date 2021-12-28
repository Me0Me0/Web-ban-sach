from peewee import *
from models.Province import Province

class ProvinceRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Province.select().offset(skip).limit(limit))


   @classmethod
   def getNameByID(cls, id: int):
       try:
           return Province.get_by_id(id)._name
       except:
           raise Exception("Does not exist province with given id")


   @classmethod
   def getIDByName(cls, name: str):
       try:
           return Province.get(Province._name == name)
       except:
           raise Exception("Does not exist province with given name")
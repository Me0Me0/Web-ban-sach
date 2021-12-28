from peewee import *
from models.Category import Category


class CategoryRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Category.select().offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):
      result = None
      for record in Category.select().where(Category.id == id):
         result = record

      return result


   @classmethod
   def create(cls, cateDict):
        return Category.create(**cateDict).id


   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_category = Category.get_by_id(id)
      except:
         raise Exception(404, {"Can not find category with given id" })

      return delete_category.delete_instance()
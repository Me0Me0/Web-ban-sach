from peewee import *
from models.Cart import Cart


class CartRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Cart.select().offset(skip).limit(limit))


   @classmethod
   def getCartID(cls, owner_id: int):
      return Cart.select().where(Cart.owner_id == owner_id)#Cart.get(Cart.owner_id == owner_id).id


   @classmethod
   def create(cls, id: int):
       return Cart.create(owner_id = id).id
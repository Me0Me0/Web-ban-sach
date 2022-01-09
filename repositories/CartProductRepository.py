from peewee import *
from configs.db import db
from models.CartProduct import CartProduct
from models.Product import Product
from models.Store import Store


class CartProductRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(CartProduct.select().offset(skip).limit(limit))


   # return a list of product [{'name': 'Tổng quan vũ trụ', 'quantity': 2, 'price': 180000.0}, {...}, ...]
   @classmethod
   def getByCartID(cls, cart_id: int):
      
      predicate1 = (CartProduct.cart_id == cart_id)
      predicate2 = (Product.id == CartProduct.product_id)
      predicate3 = (Product.store_id == Store.id)

      query = Product.select(
         CartProduct.quantity, 
         Product.id.alias('product_id'),
         Product.name, 
         Product.price, 
         Product.quantity.alias('product_quantity'),
         Store.id.alias('store_id'),
         Store.name.alias('store_name'), 
      ).join(CartProduct, on=predicate2).join(Store, on=predicate3).where(Product.deleted_at.is_null(True), predicate1).dicts()

      result = query.execute()
      return list(result)

   
   # get specific cart product
   @classmethod
   def get(cls, cart_id: int, product_id: int):
      return CartProduct.get(CartProduct.cart_id == cart_id, CartProduct.product_id == product_id)


   @classmethod
   def create(cls, cart_id: int, product_id: int, quantity: int):
       return CartProduct.create(cart_id = cart_id, product_id = product_id, quantity = quantity).id


    # product list include tuples [(product_id_1, quantity_1), (product_id_2, quantity_2), ..] 
    # example: product_list = [(2,1), (3, 1), (5,2)]
   @classmethod
   def createMany(cls, product_list):
       with db.atomic():
           CartProduct.insert_many(product_list, fields=[CartProduct.product_id, CartProduct.quantity]).execute()

   @classmethod
   def delete(cls, cart_id: int, product_id: int):
      CartProduct.delete().where(CartProduct.cart_id == cart_id, CartProduct.product_id == product_id).execute()

   
   @classmethod
   def updateQuantity(cls, cart_id: int, product_id: int, quantity: int):
      CartProduct.update(quantity=quantity).where(CartProduct.cart_id == cart_id, CartProduct.product_id == product_id).execute()
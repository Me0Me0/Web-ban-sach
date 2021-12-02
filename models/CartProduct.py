from peewee import *
from models.BModel import BModel
from models.Cart import Cart
from models.Product import Product

class CartProduct(BModel):
   cart_id=ForeignKeyField(Cart, field="id")
   product_id=ForeignKeyField(Product, field="id")
   quantity=IntegerField(index = True)

   class Meta:
      db_table='cart_product'
      primary_key = CompositeKey('cart_id', 'product_id')

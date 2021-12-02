from peewee import *
from models import BaseModel, Cart, Product
class CartProduct(BaseModel):
   cart_id=ForeignKeyField(Cart, field="id")
   product_id=ForeignKeyField(Product, field="id")
   quantity=IntegerField(index = True)

   class Meta:
      db_table='cart_product'
      primary_key = CompositeKey('cart_id', 'product_id')

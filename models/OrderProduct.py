from peewee import *
from models import BaseModel, OrderDetail, Product

class OrderProduct(BaseModel):
   order_id=ForeignKeyField(OrderDetail, field="id")
   product_id=ForeignKeyField(Product, field="id")
   quantity=IntegerField()

   class Meta:
      db_table='order_product'
      primary_key = CompositeKey('order_id', 'product_id')
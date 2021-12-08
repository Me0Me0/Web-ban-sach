from peewee import *
from models.BModel import BModel
from models.OrderDetail import OrderDetail
from models.Product import Product

class OrderProduct(BModel):
   order_id=ForeignKeyField(OrderDetail)
   product_id=ForeignKeyField(Product)
   quantity=IntegerField()

   class Meta:
      db_table='order_product'
      primary_key = CompositeKey('order_id', 'product_id')
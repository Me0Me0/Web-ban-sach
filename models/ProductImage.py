from peewee import *
from models.BModel import BModel
from models.Product import Product

class ProductImage(BModel):
    id=ForeignKeyField(Product, field="id")
    image_link=CharField()

    class Meta:
       db_table='product_image'
from peewee import *
from models import BaseModel, Product

class ProductImage(BaseModel):
    id=ForeignKeyField(Product, field="id")
    image_link=CharField()

    class Meta:
       db_table='product_image'
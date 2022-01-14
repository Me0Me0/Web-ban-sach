from peewee import *
from models.BModel import BModel
from models.Product import Product

class ProductImage(BModel):
    id=AutoField()
    product_id=ForeignKeyField(Product, backref='product_images')
    image_link=CharField()

    class Meta:
       db_table='product_image'
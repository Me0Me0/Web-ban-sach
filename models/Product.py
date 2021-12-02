from peewee import *
from models.BModel import BModel
from models.Category import Category
from models.Store import Store

class Product(BModel):

    id=AutoField()
    name=CharField()
    cate_id=ForeignKeyField(Category, field="id")
    rating=FloatField()
    description=TextField()
    detail=TextField()
    author=CharField()
    number_of_pages=IntegerField()
    publishing_year=DateField()
    publisher=CharField()
    cover_image=CharField()
    store_id=ForeignKeyField(Store, field="id")
    quantity=IntegerField()
    price=FloatField()

    class Meta:
       db_table='product'
from peewee import *
from models.BModel import BModel

class Category(BModel):
   id=AutoField()
   name=CharField()

   class Meta:
      db_table='category'
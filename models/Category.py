from enum import unique
from peewee import *
from models.BModel import BModel

class Category(BModel):
   id=AutoField()
   name=CharField(unique=True)

   class Meta:
      db_table='category'
from peewee import *
from models import BaseModel

class Cartegory(BaseModel):
   id=AutoField()
   name=CharField()

   class Meta:
      db_table='category'
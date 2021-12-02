from peewee import *
from models import BaseModel, User

class Cart(BaseModel):
   id=AutoField()
   owner=ForeignKeyField(User, field="id")

   class Meta:
      db_table='cart'
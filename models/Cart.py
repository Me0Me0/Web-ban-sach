from peewee import *
from models.BModel import BModel
from models.User import User

class Cart(BModel):
   id=AutoField()
   owner_id=ForeignKeyField(User)

   class Meta:
      db_table='cart'
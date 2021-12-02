from peewee import *
from models.BModel import BModel


class Admin(BModel):
   id=AutoField()
   username=CharField(unique=True)
   password=CharField()
   name=CharField()

   class Meta:
      db_table='admin'




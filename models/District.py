from peewee import *
from models.BModel import BModel

class District(BModel):
   id=AutoField()
   _name=CharField()
   _prefix=CharField()
   _province_id=IntegerField(index = True)


   class Meta:
      db_table='district'
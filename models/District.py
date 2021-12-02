from peewee import *
from models.BModel import BModel

class District(BModel):
   id=AutoField()
   name=CharField()
   prefix=CharField()
   province_id=IntegerField(index = True)


   class Meta:
      db_table='district'
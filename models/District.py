from peewee import *
from models import BaseModel

class District(BaseModel):
   id=AutoField()
   name=CharField()
   prefix=CharField()
   province_id=IntegerField(index = True)


   class Meta:
      db_table='district'
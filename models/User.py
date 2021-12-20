from peewee import *
from models.BModel import BModel

class User(BModel):
   id=AutoField()
   username=CharField(unique=True)
   password=CharField()
   name=CharField()
   dob= DateField()
   phone=IntegerField()
   email=CharField(unique=True)
   avt_link=CharField()
   deleted_at= DateField()

   class Meta:
      db_table='user'
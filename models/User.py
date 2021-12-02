from peewee import *
from models import BaseModel

class User(BaseModel):
   id=AutoField()
   username=CharField(unique=True)
   password=CharField()
   name=CharField()
   dob= DateTimeField()
   phone=IntegerField()
   email=CharField(unique=True)
   avt_link=CharField()

   class Meta:
      db_table='user'
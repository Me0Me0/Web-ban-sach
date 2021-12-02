from peewee import *
from models import BaseModel


class Admin(BaseModel):
   id=AutoField()
   username=CharField(unique=True)
   password=CharField()
   name=CharField()

   class Meta:
      db_table='admin'




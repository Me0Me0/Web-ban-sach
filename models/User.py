from peewee import *
from configs.db import db
from playhouse.shortcuts import ThreadSafeDatabaseMetadata

class BaseModel(Model):
    class Meta:
       database = db
       # Instruct peewee to use our thread-safe metadata implementation.
       model_metadata_class = ThreadSafeDatabaseMetadata

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
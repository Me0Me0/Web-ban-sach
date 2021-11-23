from peewee import *
from configs.db import db
from playhouse.shortcuts import ThreadSafeDatabaseMetadata

class BaseModel(Model):
    class Meta:
       database = db
       # Instruct peewee to use our thread-safe metadata implementation.
       model_metadata_class = ThreadSafeDatabaseMetadata

class User(BaseModel):
   id=IntegerField(primary_key=True)
   username=CharField()
   password=CharField()
   name=CharField()
   dob= DateTimeField()
   address=CharField()
   phone=IntegerField()
   email=CharField()
   avt_link=CharField()

   class Meta:
      db_table='user'
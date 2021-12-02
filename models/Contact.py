from peewee import *
from models import BaseModel, User

class Contact(BaseModel):
   id=AutoField()
   user_id=ForeignKeyField(User, field="id")
   create=DateTimeField()
   title=CharField()
   content=TextField()
   status=IntegerField()

   class Meta:
      db_table='contact'
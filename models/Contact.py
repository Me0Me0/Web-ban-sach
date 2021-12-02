from peewee import *
from models.BModel import BModel
from models.User import User

class Contact(BModel):
   id=AutoField()
   user_id=ForeignKeyField(User, field="id")
   create=DateTimeField()
   title=CharField()
   content=TextField()
   status=IntegerField()

   class Meta:
      db_table='contact'
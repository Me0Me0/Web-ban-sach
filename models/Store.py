from peewee import *
from models import BaseModel, User

class Store(BaseModel):
    id=AutoField()
    name=CharField()
    owner=ForeignKeyField(User, field="id")
    phone=IntegerField()
    email=CharField()
    rating=FloatField()
    description=TextField()

    class Meta:
       db_table='store'
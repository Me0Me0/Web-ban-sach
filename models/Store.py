from peewee import *
from models.BModel import BModel
from models.User import User

class Store(BModel):
    id=AutoField()
    name=CharField()
    owner=ForeignKeyField(User, field="id")
    phone=IntegerField()
    email=CharField()
    rating=FloatField()
    description=TextField()

    class Meta:
       db_table='store'
from peewee import *
from models.BModel import BModel
from models.User import User

class Store(BModel):
    id=AutoField()
    name=CharField(unique=True)
    owner_id=ForeignKeyField(User)
    phone=IntegerField()
    email=CharField()
    rating=FloatField()
    description=TextField()

    class Meta:
       db_table='store'
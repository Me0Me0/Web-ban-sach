from peewee import *
from models.BModel import BModel

class Province(BModel):
    id=AutoField()
    name=CharField()
    code=CharField()

    class Meta:
       db_table='province'
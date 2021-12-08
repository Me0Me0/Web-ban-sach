from peewee import *
from models.BModel import BModel

class Province(BModel):
    id=AutoField()
    _name=CharField()
    _code=CharField()

    class Meta:
       db_table='province'
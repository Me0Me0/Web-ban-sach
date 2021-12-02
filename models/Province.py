from peewee import *
from models import BaseModel

class Province(BaseModel):
    id=AutoField()
    name=CharField()
    code=CharField()

    class Meta:
       db_table='province'
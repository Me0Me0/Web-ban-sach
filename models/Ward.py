from peewee import *
from models.BModel import BModel

class Ward(BModel):
    id=AutoField()
    name=CharField()
    prefix=CharField()
    province_id=IntegerField(index = True)
    district_id=IntegerField(index = True)

    class Meta:
       db_table='ward'
       indexes = (
            (('province_id', 'district_id'), False),
        )
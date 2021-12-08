from peewee import *
from models.BModel import BModel

class Ward(BModel):
    id=AutoField()
    _name=CharField()
    _prefix=CharField()
    _province_id=IntegerField(index = True)
    _district_id=IntegerField(index = True)

    class Meta:
       db_table='ward'
       indexes = (
            (('province_id', 'district_id'), False),
        )
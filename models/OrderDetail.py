from peewee import *
from models.BModel import BModel
from models.User import User
from models.Province import Province
from models.District import District
from models.Ward import Ward

class OrderDetail(BModel):
   id=AutoField()
   owner_id=ForeignKeyField(User)

   status=IntegerField()
   total_cost=FloatField()

   recipient_name=CharField()
   recipient_phone=IntegerField()
   recipient_address=CharField()
   
   province_id=ForeignKeyField(Province)
   district_id=ForeignKeyField(District)
   ward_id=ForeignKeyField(Ward)


   class Meta:
      db_table='order_detail'
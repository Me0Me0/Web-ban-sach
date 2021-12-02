from peewee import *
from models.BModel import BModel
from models.User import User
from models.Province import Province
from models.District import District
from models.Ward import Ward

class OrderDetail(BModel):
   id=IntegerField()
   owner=ForeignKeyField(User, field="id")

   status=IntegerField()
   total_cost=FloatField()

   recipient_name=CharField()
   recipient_phone=IntegerField()
   recipient_address=CharField()
   
   province_id=ForeignKeyField(Province, field="id")
   district_id=ForeignKeyField(District, field="id")
   ward_id=ForeignKeyField(Ward, field="id")


   class Meta:
      db_table='order_detail'
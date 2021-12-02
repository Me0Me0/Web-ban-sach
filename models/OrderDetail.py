from peewee import *
from models import BaseModel, User, Province, District, Ward

class OrderDetail(BaseModel):
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
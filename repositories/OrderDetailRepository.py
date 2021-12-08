from peewee import *
from models.OrderDetail import OrderDetail
from models.User import User
from models.Province import Province
from models.District import District
from models.Ward import Ward


class OrderDetailRepository():

    @classmethod
    def getAll(cls, skip: int = 0, limit: int = 100):
        return list(OrderDetail.select().offset(skip).limit(limit))


    @classmethod
    def getByUserId(cls, user_id, skip: int = 0, limit: int = 100):
        return list(OrderDetail.select().where(OrderDetail.owner_id == user_id).offset(skip).limit(limit))


    @classmethod
    def create(cls, orderDict):
        return OrderDetail.create(**orderDict).id


    @classmethod
    def saveCreate(cls, user_id, province_id, district_id, ward_id, orderDict):
        try:
            user = User.get_by_id(user_id)
        except:
            raise Exception(404, { "ERROR": "Can not find user with given id" })


        try:
            province = Province.get_by_id(province_id)
        except:
            raise Exception(404, { "ERROR": "Can not find province with given id" })


        try:
            district = District.get_by_id(district_id)
        except:
            raise Exception(404, { "ERROR": "Can not find district with given id" })


        try:
            ward = Ward.get_by_id(ward_id)
        except:
            raise Exception(404, { "ERROR": "Can not find ward with given id" })

        return OrderDetail.create(owner_id = user, province_id = province, district_id = district, ward_id = ward, **orderDict).id


    @classmethod
    def deleteById(cls, id: int):
       try:
          delete_order = OrderDetail.get_by_id(id)
       except:
          raise Exception(404, { "DELETE ERROR": "Can not find order with given id" })

       return delete_order.delete_instance()

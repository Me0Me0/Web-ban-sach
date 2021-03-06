from peewee import *
from models.CartProduct import CartProduct
from models.OrderDetail import OrderDetail
from models.OrderProduct import OrderProduct
from models.User import User
from models.Province import Province
from models.District import District
from models.Product import Product
from models.Ward import Ward
from configs.db import db


class OrderDetailRepository():

    @classmethod
    def getAll(cls, skip: int = 0, limit: int = 100):
        return list(OrderDetail.select().offset(skip).limit(limit))


    @classmethod
    def getByUserId(cls, user_id, skip: int = 0, limit: int = 100):
        return list(OrderDetail.select().where(OrderDetail.owner_id == user_id).offset(skip).limit(limit))


    @classmethod
    def getByStoreId(cls, store_id, skip: int = 0, limit: int = 100):
        return list(OrderDetail.select().where(OrderDetail.store_id == store_id).offset(skip).limit(limit))
    
    
    @classmethod
    def getByIdList(cls, id_list):
        return list(OrderDetail.select().where(OrderDetail.id.in_(id_list)))


    @classmethod
    def getById(cls, id_order: int):
        return OrderDetail.get_by_id(id_order)


    @classmethod
    def create(cls, orderDict):
        return OrderDetail.create(**orderDict).id


    # status = 1: Đang xử lý, 2: Đang giao hàng, 3: Đã hoàn thành, 4: Đơn hàng bị hủy
    @classmethod
    def createOrdersTransaction(cls, user_id, province_id, district_id, ward_id, 
                                    recipient_name, recipient_phone, recipient_address, orderByStore):

        with db.atomic() as transaction:
            try:
                for store_id, info in orderByStore.items():
                    order_id = OrderDetail.create(
                        owner_id = user_id, 
                        store_id = store_id,
                        recipient_name = recipient_name, 
                        recipient_phone = recipient_phone, 
                        recipient_address = recipient_address,
                        province_id = province_id, 
                        district_id = district_id, 
                        ward_id = ward_id, 
                        status = 1, 
                        total_cost = info['total_cost'], 
                    ).id

                    for item in info['items']:
                        nUpdate = Product.update(quantity = Product.quantity - item.quantity).where(
                            Product.id == item.product_id,
                            Product.deleted_at == None,
                            Product.quantity >= item.quantity,
                        ).execute()
                        
                        if nUpdate == 0 or item.quantity <= 0: 
                            raise Exception(422, "Invalid quantity")
                        OrderProduct.create(order_id = order_id, product_id = item.product_id, quantity = item.quantity)      
                        CartProduct.delete().where(CartProduct.cart_id == item.cart_id, CartProduct.product_id == item.product_id).execute()
                        
                        # reduce quantity of users' cart product if it's quantity >  product quantity
                        product = Product.get_by_id(item.product_id)
                        CartProduct.update(quantity = product.quantity).where(
                            CartProduct.product_id == item.product_id, 
                            CartProduct.quantity > product.quantity
                        ).execute()

                transaction.commit()
                return True

            except Exception as e:
                transaction.rollback()
                raise e
                

    @classmethod
    def saveCreate(cls, user_id, province_id, district_id, ward_id, orderDict):
        try:
            user = User.get_by_id(user_id)
        except:
            raise Exception("Can not find user with given id")


        try:
            province = Province.get_by_id(province_id)
        except:
            raise Exception("Can not find province with given id")


        try:
            district = District.get_by_id(district_id)
        except:
            raise Exception("Can not find district with given id")


        try:
            ward = Ward.get_by_id(ward_id)
        except:
            raise Exception("Can not find ward with given id")

        return OrderDetail.create(owner_id = user, province_id = province, district_id = district, ward_id = ward, **orderDict).id


    @classmethod
    def deleteById(cls, id: int):
       try:
          delete_order = OrderDetail.get_by_id(id)
       except:
          raise Exception("Can not find order with given id")

       return delete_order.delete_instance()

    
    @classmethod
    def setStatus(cls, id: int, status: int):
        try:
            update_order = OrderDetail.get_by_id(id)
        except:
            raise Exception("Can not find order with given id")
        update_order.status = status
        return update_order.save()

from peewee import *
from configs.db import db
from models.OrderProduct import OrderProduct
from models.OrderDetail import OrderDetail
from models.Product import Product


class OrderProductRepository():

    @classmethod
    def getAll(cls, skip: int = 0, limit: int = 100):
        return list(OrderProduct.select().offset(skip).limit(limit))


    @classmethod
    def create(cls, orderDict):
        return OrderProduct.create(**orderDict).id


    @classmethod
    def saveCreate(cls, order_id, product_id, orderDict):
        try:
            order = OrderDetail.get_by_id(order_id)
        except:
            raise Exception("Can not find order with given id")


        try:
            product = Product.get_by_id(product_id)
        except:
            raise Exception("Can not find product with given id" )


        try:
            return OrderProduct.create(order_id = order, product_id = product, **orderDict)
        except Exception as e:
            if e.args[0] == 1062:
                raise Exception("Order with id: {} already has product with id: {}".format(order_id, product_id))


    # product list include tuples [(order_id_1, product_id_1), (order_id_2, product_id_2), ..] 
    @classmethod
    def createMany(cls, product_list):
        with db.atomic:
            OrderProduct.insert_many(product_list, fields=[OrderProduct.order_id, OrderProduct.product_id]).execute()


    @classmethod
    def deleteById(cls, id: int):
       try:
          delete_order = OrderProduct.get_by_id(id)
       except:
          raise Exception("Can not find order with given id")

       return delete_order.delete_instance()

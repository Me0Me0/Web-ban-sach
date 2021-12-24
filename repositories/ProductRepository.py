from peewee import *
from models.Product import Product
from models.Store import Store
from models.Category import Category
from models.OrderDetail import OrderDetail
from models.OrderProduct import OrderProduct


class ProductRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Product.select().offset(skip).limit(limit))


   @classmethod
   def getByName(cls, name: str, skip: int = 0, limit: int = 100):
      return list(Product.select().where(Product.name == name).offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):
       try:
           return Product.get_by_id(id)
       except:
           raise Exception(404, { "ERROR": "Does not exist product with given id"})


   @classmethod
   def getByStore(cls, store_id: int, skip: int = 0, limit: int = 100):
       return list(Product.select().join(Store).where(Store.id == store_id))


   @classmethod
   def getSortByDate(cls, ascending: bool = True, skip: int = 0, limit: int = 100):
       if ascending:
           return list(Product.select().order_by(Product.publishing_year).offset(skip).limit(limit))
       else:
           return list(Product.select().order_by(Product.publishing_year.desc()).offset(skip).limit(limit))


   @classmethod
   def getSortBySell(cls, ascending: bool = False, skip: int = 0, limit: int = 100):
       if ascending:
           return list(Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity).desc()).offset(skip).limit(limit))
       else:
           return list(Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity).desc()).offset(skip).limit(limit))
      

   @classmethod
   def create(cls, store_id: int, productDict):#category: str, productDict):
       try:
           store = Store.get_by_id(store_id)
       except:
           raise Exception(404, { "ERROR": "Can not find store with given id" })


       try:
           cate = Category.get(Category.name == productDict['category'])
           #cate = Category.get(Category.name == category)
       except:
           raise Exception(404, { "ERROR": "Category does not exist" })

       return Product.create(cate_id = cate, store_id = store, **productDict).id


   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_product = Product.get_by_id(id)
      except:
         raise Exception(404, { "DELETE ERROR": "Can not find product with given id" })

      return delete_product.delete_instance()
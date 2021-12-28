from peewee import *
from peewee import datetime
from datetime import timedelta
from models.Product import Product
from models.Store import Store
from models.Category import Category
from models.OrderProduct import OrderProduct


class ProductRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(Product.select().where(Product.deleted_at.is_null(True)).offset(skip).limit(limit))


   @classmethod
   def getDeletedProduct(cls, skip: int = 0, limit: int = 100):
      return list(Product.select().where(Product.deleted_at.is_null(False)).offset(skip).limit(limit))


   @classmethod
   def getByName(cls, name: str, skip: int = 0, limit: int = 100):
      return list(Product.select().where((Product.name == name) & (Product.deleted_at.is_null(True))).offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):
       try:
           return Product.get_by_id(id)
       except:
           raise Exception("Does not exist product with given id")


   @classmethod
   def getByStore(cls, store_id: int, skip: int = 0, limit: int = 100):
       return list(Product.select().join(Store).where((Store.id == store_id) & (Product.deleted_at.is_null(True))))


   @classmethod
   def getSortByDate(cls, ascending: bool = True, skip: int = 0, limit: int = 100):
       if ascending:
           return list(Product.select().where(Product.deleted_at.is_null(True)).order_by(Product.publishing_year).offset(skip).limit(limit))
       else:
           return list(Product.select().where(Product.deleted_at.is_null(True)).order_by(Product.publishing_year.desc()).offset(skip).limit(limit))


   @classmethod
   def getSortBySell(cls, ascending: bool = False, skip: int = 0, limit: int = 100):
       if ascending:
           return list(Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct).where(Product.deleted_at.is_null(True)).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity)).offset(skip).limit(limit))
       else:
           return list(Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct).where(Product.deleted_at.is_null(True)).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity).desc()).offset(skip).limit(limit))
      

   @classmethod
   def create(cls, store_id: int, category: str, productDict):
       try:
           store = Store.get_by_id(store_id)
       except:
           raise Exception("Can not find store with given id")


       try:
           cate = Category.get(Category.name == category)
       except:
           raise Exception("Category does not exist")

       return Product.create(cate_id = cate, store_id = store, **productDict).id


   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_product = Product.get_by_id(id)
      except:
         raise Exception("Can not find product with given id")

      if (delete_product.deleted_at != None):
          return 0
          
      delete_product.deleted_at = datetime.datetime.now().date()

      return delete_product.save()


   @classmethod
   def deleteByStoreId(cls, id: int):
      count = Product.update({Product.deleted_at: datetime.datetime.now().date()}).where(Product.store_id == id).execute()
      return count


   # Delete from DB, only Admin use this method
   @classmethod
   def deleteFromDB(cls,max_day: int = 30):
      query = Product.delete().where(Product.deleted_at <= datetime.datetime.now().date() - timedelta(days=max_day))

      return query.execute()
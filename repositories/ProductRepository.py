from peewee import *
from peewee import datetime
from datetime import timedelta
from models.Product import Product
from models.Store import Store
from models.Category import Category
from models.OrderProduct import OrderProduct
from models.OrderDetail import OrderDetail


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
   def getByCate(cls, cate_id: int, skip: int = 0, limit: int = 100):
      return list(Product.select().where((Product.cate_id == cate_id) & (Product.deleted_at.is_null(True))).offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):
       try:
           product = Product.get_by_id(id)
           if product.deleted_at is None:
               return product
           raise Exception("Product is deleted")
       except:
           raise Exception("Does not exist product with given id")


    # id_list = [1,2,3,..]
   @classmethod
   def getByIdList(cls, id_list):
       return list(Product.select().where(Product.id.in_(id_list) & Product.deleted_at.is_null(True)))


   @classmethod
   def getByStore(cls, store_id: int, skip: int = 0, limit: int = 100):
       return list(Product.select().join(Store).where((Store.id == store_id) & (Product.deleted_at.is_null(True))).offset(skip).limit(limit))


   @classmethod
   def getSortByDate(cls, ascending: bool = False, skip: int = 0, limit: int = 100):
       if ascending:
           return list(Product.select().where(Product.deleted_at.is_null(True)).order_by(Product.publishing_year).offset(skip).limit(limit))
       else:
           return list(Product.select().where(Product.deleted_at.is_null(True)).order_by(Product.publishing_year.desc()).offset(skip).limit(limit))


   @classmethod
   def getSortBySell(cls, ascending: bool = False, status: int = 3, skip: int = 0, limit: int = 100):
       if ascending:
           return list(Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct, JOIN.LEFT_OUTER).join(OrderDetail).where((OrderDetail.status == status) & Product.deleted_at.is_null(True)).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity)).offset(skip).limit(limit))
       else:
           return list(Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct, JOIN.LEFT_OUTER).join(OrderDetail).where((OrderDetail.status == status) & Product.deleted_at.is_null(True)).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity).desc()).offset(skip).limit(limit))


    # Lấy danh sách danh mục bán chạy nhất trên hệ thống
   @classmethod
   def getTopCate(cls, status: int = 3, skip: int = 0, limit: int = 10):
       subquery = Product.select(Product.cate_id).join(OrderProduct, JOIN.LEFT_OUTER).join(OrderDetail).where((OrderDetail.status == status) & Product.deleted_at.is_null(True)).group_by(Product.cate_id).order_by(fn.SUM(OrderProduct.quantity).desc())
       query = Category.select().where(Category.id.in_(subquery)).offset(skip).limit(limit)
       return list(query.execute())


    # Lấy danh sách sản phẩm bán chạy nhất của một cửa hàng
   @classmethod
   def getBestSellByStore(cls, store_id: int, status: int = 3, skip: int = 0, limit: int = 10):
       query = Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct, JOIN.LEFT_OUTER).join(OrderDetail).where((OrderDetail.status == status) & (Product.store_id == store_id) & Product.deleted_at.is_null(True)).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity).desc()).offset(skip).limit(limit)
       return list(query.execute())


    # Lấy danh sách danh mục bán chạy nhất của một cửa hàng
   @classmethod
   def getBestSellByCate(cls, store_id: int, status: int = 3, skip: int = 0, limit: int = 10):
       query = Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct, JOIN.LEFT_OUTER).join(OrderDetail).where((OrderDetail.status == status) & (Product.store_id == store_id) & Product.deleted_at.is_null(True)).group_by(Product.cate_id).order_by(fn.SUM(OrderProduct.quantity).desc()).offset(skip).limit(limit)
       return list(query.execute())


   @classmethod
   def searchByName(cls, name: str, field: str = "", ascending: bool = False, skip: int = 0, limit: int = 100):
       tokens = name.split()
       search_name = ""
       for i in tokens:
           search_name = search_name + "%" + i + "%"

       if(field == ""):
           query = Product.select().where((Product.name ** search_name) & (Product.deleted_at.is_null(True))).offset(skip).limit(limit)
       else:
           if ascending:
                query = Product.select().where((Product.name ** search_name) & (Product.deleted_at.is_null(True))).order_by(SQL(field)).offset(skip).limit(limit)
           else:
                query = Product.select().where((Product.name ** search_name) & (Product.deleted_at.is_null(True))).order_by(SQL(field).desc()).offset(skip).limit(limit)

       try:     
           return list(query.execute())
       except:
           raise Exception("Invalid field")


   @classmethod
   def inOrderWithStatus(cls, product_id: int, skip: int = 0, limit: int = 100):
       query = OrderProduct.select().join(OrderDetail).where(OrderProduct.product_id == product_id & (OrderDetail.status == 1 | OrderDetail.status == 2 ))

       return [item.order_id.id for item in query]


   @classmethod
   def create(cls, store_id: int, category_id: int, productDict):
       try:
           store = Store.get_by_id(store_id)
       except:
           raise Exception("Can not find store with given id")


       try:
           cate = Category.get_by_id(category_id)
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
    
    
   @classmethod
   def update(cls, product_id: int, productDict):
       try:
         update_product = Product.get_by_id(product_id)
       except:
         raise Exception("Can not find product with given id")


       try:
           cate = Category.get_by_id(productDict["cate_id"])
       except:
           raise Exception("Category does not exist")

       update_product.name = productDict["name"]
       update_product.cate_id = cate
       update_product.description = productDict["description"]
       update_product.detail = productDict["detail"]
       update_product.author = productDict["author"]
       update_product.number_of_pages = productDict["number_of_pages"]
       update_product.publishing_year = productDict["publishing_year"]
       update_product.publisher = productDict["publisher"]
       update_product.cover_image = productDict["cover_image"]
       update_product.quantity = productDict["quantity"]
       update_product.price = productDict["price"]

       return update_product.save()


   @classmethod
   def updatePrice(cls, product_id: int, price: float):
       try:
         update_product = Product.get_by_id(product_id)
       except:
         raise Exception("Can not find product with given id")

       update_product.price = price

       return update_product.save()


   @classmethod
   def updateQuantity(cls, product_id: int, quantity: int):
       try:
         update_product = Product.get_by_id(product_id)
       except:
         raise Exception("Can not find product with given id")

       update_product.quantity = quantity

       return update_product.save()


   @classmethod
   def updateQuantity2(cls, product_id: int, quantity_diff: int):
       try:
         update_product = Product.get_by_id(product_id)
       except:
         raise Exception("Can not find product with given id")

       update_product.quantity = update_product.quantity + quantity_diff

       return update_product.save()

   @classmethod
   def updateImage(cls, product_id: int, image_link: str):
       try:
         update_product = Product.get_by_id(product_id)
       except:
         raise Exception("Can not find product with given id")

       update_product.cover_image = image_link

       return update_product.save()


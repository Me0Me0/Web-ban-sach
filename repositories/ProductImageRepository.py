from peewee import *
from configs.db import db
from models.ProductImage import ProductImage
from models.Product import Product



class ProductImageRepository():

   @classmethod
   def getByProduct(cls, product_id: int, skip: int = 0, limit: int = 5):
      return list(ProductImage.select().join(Product).where((Product.id == product_id) & Product.deleted_at.is_null(True)).offset(skip).limit(limit))


   @classmethod
   def create(cls, product_id: int, image: str):
       try:
           product = Product.get_by_id(product_id)
       except:
           raise Exception("Can not find product with given id")

       return ProductImage.create(product_id = product, image_link = image)


   # image list include tuples [(product_id_1, image_link_1), (product_id_2, image_link_2), ..] 
   # example: product_list = [(1,https://abc), (1, https://zyec), (2,https://mcmdj)]
   @classmethod
   def createMany(cls, image_list):
       with db.atomic():
           ProductImage.insert_many(image_list, fields=[ProductImage.product_id, ProductImage.image_link]).execute()


   @classmethod
   def updateImage(cls, id: int, newImage: str):
       return ProductImage.update(image_link = newImage).where(ProductImage.id == id)

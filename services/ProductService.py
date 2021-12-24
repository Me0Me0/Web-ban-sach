from datetime import datetime
from repositories.ProductRepository import ProductRepository
from schemas import product_schema
from configs.constant import DEFAULT_AVT


class ProductService:
        
    @classmethod
    def getById(cls, id):
        return ProductRepository.getById(id)
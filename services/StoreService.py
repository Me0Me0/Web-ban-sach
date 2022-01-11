from fastapi import APIRouter
from repositories.StoreRepository import StoreRepository
from repositories.UserRepository import UserRepository
from repositories.ProductRepository import ProductRepository
from repositories.OrderDetailRepository import OrderDetailRepository
from repositories.OrderProductRepository import OrderProductRepository
from schemas import store_schema
from schemas import product_schema
from configs.constant import DEFAULT_AVT

class StoreService:

    @classmethod
    def getOwnStore(cls, user_id):
        stores = StoreRepository.getByUserId(user_id)
        if len(stores) == 0:
            raise Exception(404, "not found")
        return stores[0].__data__


    @classmethod
    def registerStore(cls, user_id):
        user = UserRepository.getById(user_id)
        if not user: 
            raise Exception(404, "not found")

        stores = StoreRepository.getByUserId(user_id)
        if len(stores) > 0:
            raise Exception(409, "already exists")

        store = {
            "name": user.username,
            "owner_id": user.id,
            "phone": user.phone,
            "email": user.email,
            "rating": 0,
            "description": ""
        }
        return StoreRepository.create(store)


    @classmethod
    def createProduct(cls, payload: product_schema.ProductCreate, store_id):
        productDict = payload.__dict__
        productDict['avt_link'] = DEFAULT_AVT
        # Get category of product
        category = productDict['cate_id']
        # Remove category field from productDict 
        del productDict['cate_id']
        return ProductRepository.create(store_id, category, productDict)

    
    @classmethod
    def getAll(cls, skip, limit, store_id):
        return [StoreRepository.getById(store_id), ProductRepository.getByStore(store_id, skip, limit)]

    @classmethod  
    def getStoreDetail(cls, store_id):
        return StoreRepository.getById(store_id)

    
    @classmethod
    def getStoreProduct(cls, skip, limit, store_id):
        return ProductRepository.getByStore(store_id, skip, limit)


    @classmethod
    def cancelOrder(cls, user_id, order_id):
        try:
            store_id = StoreRepository.getByUserId(user_id)
            eraser_id = OrderDetailRepository.getById(order_id).store_id
        except Exception as e:
            raise Exception(404, "Invalid store")

        if store_id[0].id != eraser_id.id:
            raise Exception(403, "Forbidden")
        
        # Set OrderDetail status
        try:
            OrderDetailRepository.setStatus(order_id, 4) # 4 ~ Da huy
        except Exception as e:
            raise Exception(e)
        
        products = OrderProductRepository.getByOrderID(order_id)
        
        # Refund quality products
        try:
            for product in products:
                ProductRepository.updateQuantity2(product.product_id, product.quantity)
        except Exception as e:
            raise Exception(e)


    @classmethod
    def getBestSellCate(cls, store_id):
        return ProductRepository.getBestSellByCate(store_id)

    
    @classmethod
    def getBestSellProducts(cls, store_id):
        return ProductRepository.getBestSellByStore(store_id)


    @classmethod
    def getTotalIncome(cls, store_id):
        return StoreRepository.getTotalIncome(store_id)


    @classmethod
    def update(cls, user_id, payload):
        try:
            return StoreRepository.updateByUserID(user_id, payload.__dict__)
        except Exception as e:
            raise Exception(409, "Duplicated email")


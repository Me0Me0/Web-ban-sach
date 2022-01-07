from repositories.CartProductRepository import CartProductRepository
from repositories.CartRepository import CartRepository
from repositories.OrderDetailRepository import OrderDetailRepository
from repositories.OrderProductRepository import OrderProductRepository
from repositories.ProductRepository import ProductRepository
from repositories.ProvinceRepository import ProvinceRepository
from repositories.DistrictRepository import DistrictRepository
from repositories.WardRepository import WardRepository

class OrderService:

    @classmethod
    def getOwnOrders(cls, user_id, limit, skip):
        orders = OrderDetailRepository.getByUserId(user_id, skip, limit)
        return orders

    
    @classmethod
    def createOrder(cls, payload, user_id):
        try:
            ProvinceRepository.getNameByID(payload.province_id)
            DistrictRepository.getByID(payload.district_id)
            WardRepository.getByID(payload.ward_id)
        except Exception as e:
            raise Exception(422, "Invalid province, district or ward")

        if len(payload.products) == 0:
            raise Exception(422, "Cart is empty")

        ordersByStore = {}
        for item in payload.products:
            try:
                product = ProductRepository.getById(item.product_id)
            except Exception as e:
                raise Exception(422, "Invalid product")

            try:
                cart_id = CartRepository.getCartID(user_id)
                cartItem = CartProductRepository.get(cart_id, item.product_id)
            except Exception as e:
                raise Exception(422, "Invalid cart")

            if product.store_id not in ordersByStore:
                ordersByStore[product.store_id] = {
                    'total_cost': product.price * cartItem.quantity,
                    'items': [ cartItem ]
                }
            else:
                ordersByStore[product.store_id]['total_cost'] += product.price * cartItem.quantity
                ordersByStore[product.store_id]['items'].append(cartItem)
        
        return OrderDetailRepository.createOrdersTransaction(
            user_id = user_id,
            province_id = payload.province_id,
            district_id = payload.district_id,
            ward_id = payload.ward_id,
            recipient_name = payload.recipient_name,
            recipient_phone = payload.recipient_phone,
            recipient_address = payload.recipient_address,
            orderByStore = ordersByStore 
        )
        
        
    @classmethod
    def getProducts(cls, user_id):#, limit, skip):
        orders = OrderProductRepository.getAll()#getByOrderID(user_id)#, skip, limit)
        return orders

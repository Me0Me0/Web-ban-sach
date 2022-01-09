from repositories.CartProductRepository import CartProductRepository
from repositories.CartRepository import CartRepository
from repositories.OrderDetailRepository import OrderDetailRepository
from repositories.OrderProductRepository import OrderProductRepository
from repositories.ProductRepository import ProductRepository
from repositories.StoreRepository import StoreRepository
from repositories.ProvinceRepository import ProvinceRepository
from repositories.DistrictRepository import DistrictRepository
from repositories.WardRepository import WardRepository

class OrderService:

    @classmethod
    def getOwnOrders(cls, user_id, limit, skip):
        orders = OrderDetailRepository.getByUserId(user_id, skip, limit)
        return orders


    @classmethod
    def getStoreOrders(cls, user_id, limit, skip):
        stores = StoreRepository.getByUserId(user_id)[0]
        orders = OrderDetailRepository.getByStoreId(stores.id, skip, limit)
        return orders


    @classmethod
    def getByOrderID(cls, order_id):
        return OrderDetailRepository.getById(order_id)


    @classmethod
    def createOrder(cls, payload, user_id):
        # check address
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
            # check product existance
            try:
                product = ProductRepository.getById(item.product_id)
            except Exception as e:
                raise Exception(422, "Invalid product")

            # check item cart existance
            try:
                cart_id = CartRepository.getCartID(user_id)
                cartItem = CartProductRepository.get(cart_id, item.product_id)
            except Exception as e:
                raise Exception(422, "Invalid cart")

            # check cart item quantity
            if cartItem.quantity != item.quantity:
                raise Exception(422, "Invalid quantity")

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

        
    @classmethod
    def getByListOrderID(cls, list_orders, skip, limit):
        products_list = []
        for order in list_orders:
            rslt = OrderProductRepository.getByOrderID(order.id, skip, limit)
            # Vì rslt là kiểu list nên phải lấy từng phần tử ra để cho
            # products_list chỉ gồm các order_product chứ không phải gồm list các order_product
            if len(rslt) >= 1:
                for i in range(len(rslt)):
                    products_list.append(rslt[i])
        return products_list


    @classmethod
    def cancelOrder(cls, user_type, user_id, order_id):
        # User
        if user_type == 1:
            try:
                eraser_id = OrderDetailRepository.getById(order_id).owner_id
            except Exception as e:
                raise Exception(404, "Invalid user")

        # Store    
        elif user_type == 2:
            try:
                store_id = StoreRepository.getByUserId(user_id)
                eraser_id = OrderDetailRepository.getById(order_id).store_id
            except Exception as e:
                raise Exception(404, "Invalid store")
                
        if (user_type == 1 and user_id != eraser_id.id) or (user_type == 2 and store_id[0].id != eraser_id.id):
            raise Exception(403, "Forbidden")
        
        # Set OrderDetail status
        try:
            OrderDetailRepository.setStatus(order_id, 4) # 4 ~ Da huy
        except Exception as e:
            raise Exception(e)
        
        # Refund quality products
        try:
            print(OrderProductRepository.cancelOrder(order_id))
        except Exception as e:
            raise Exception(e)
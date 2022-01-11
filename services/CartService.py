from repositories.CartRepository import CartRepository
from repositories.UserRepository import UserRepository
from repositories.CartProductRepository import CartProductRepository
from repositories.ProductRepository import ProductRepository

class CartService:

    @classmethod
    def getOwnCart(cls, user_id):
        cart_id = CartRepository.getCartID(user_id)
        # if len(cart) == 0:
        #     raise Exception(404, "not found")
        return cart_id

    @classmethod
    def createCart(cls, user_id):
        user = UserRepository.getById(user_id)
        if not user:
            raise Exception(404, "not found")
        
        cart = CartRepository.getCartID(user_id)
        if len(cart) > 0:
            raise Exception(409, "already exists")

        return CartRepository.create(user_id)
        

    @classmethod
    def getAll(cls, cart_id):
        return CartProductRepository.getByCartID(cart_id)


    @classmethod
    def deleteProduct(cls, cart_id, product_id):
        CartProductRepository.delete(cart_id, product_id)


    @classmethod
    def updateQuantity(cls, cart_id, product_id, quantity):
        try:
            product = ProductRepository.getById(product_id)
        except:
            raise Exception(422, "Invalid product")

        if quantity > product.quantity:
            raise Exception(422, "Invalid quantity")
        CartProductRepository.updateQuantity(cart_id, product_id, quantity)
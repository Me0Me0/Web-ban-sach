from repositories.CartRepository import CartRepository

class CartService:

    @classmethod
    def createCart(cls, user_id):
        return CartRepository.create(user_id)
        
    @classmethod
    def getCartID(cls, id):
       return CartRepository.getCartID(id)
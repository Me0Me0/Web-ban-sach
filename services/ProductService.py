from repositories.ProductRepository import ProductRepository
from repositories.StoreRepository import StoreRepository


class ProductService:

    @classmethod
    def delete(cls, id, user_id):
        stores = StoreRepository.getByUserId(user_id)
        product = ProductRepository.getById(id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")

        ProductRepository.deleteById(id)
        

            
            
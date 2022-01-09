from datetime import datetime
from repositories.ProductRepository import ProductRepository
from repositories.ProductImageRepository import ProductImageRepository
from repositories.StoreRepository import StoreRepository
from repositories.CategoryRepository import CategoryRepository
from repositories.CartProductRepository import CartProductRepository
from fastapi.exceptions import HTTPException
from schemas import product_schema
from configs.constant import DEFAULT_AVT


class ProductService:

    @classmethod
    def getById(cls, id):
        return ProductRepository.getById(id)

    
    @classmethod
    def delete(cls, id, user_id):
        stores = StoreRepository.getByUserId(user_id)
        product = ProductRepository.getById(id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")

        # Các order có sản phẩm này và đang trong status 1 hoặc 2
        productsOnOrder = ProductRepository.inOrderWithStatus(id)
        if len(productsInOrder) > 0:
            raise Exception(403, "Can't delete, products are currently on order")
        
        ProductRepository.deleteById(id)
        

    @classmethod
    def update(cls, user_id, product_id, payload):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")

        return ProductRepository.update(product_id, payload.__dict__)


    @classmethod
    def updateCoverImage(cls, user_id, product_id, image_link):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")
        
        return ProductRepository.updateImage(product_id, image_link)
        
    
    @classmethod
    def updateImage(cls, user_id, product_id, list_image_link):
        product = ProductRepository.getById(product_id)
        stores = StoreRepository.getByUserId(user_id)

        if len(stores) == 0 or product.store_id != stores[0]:
            raise Exception(403, "forbidden")
        
        image_list = []
        for image_link in range(len(list_image_link)):
            image_list.append((product_id, image_link))
        
        return ProductImageRepository.createMany(image_list)
        
    
    @classmethod
    def addToCart(cls, cart_id, product_id, quantity):
        return CartProductRepository.create(cart_id, product_id, quantity)


    @classmethod
    def getProductNew(cls, ascending, skip, limit):
        return ProductRepository.getSortByDate(ascending, skip, limit)


    @classmethod
    def getTopProduct(cls, ascending, skip, limit):
        return ProductRepository.getSortBySell(ascending, skip, limit)


    @classmethod
    def getProductByName(cls, name):
        return ProductRepository.getByName(name)


    @classmethod
    def getProductByCategory(cls, cate_id, skip, limit):
        category = CategoryRepository.getById(cate_id)
        if not category:
            raise HTTPException(status_code=404, detail="")
        return ProductRepository.getByCate(cate_id, skip, limit)


    @classmethod
    def searchProduct(cls, keyword, category, maxPrice, minPrice, order, sortBy):
        products_rslt = ProductRepository.searchByName(keyword)

        if len(products_rslt) == 0: # Không có kết quả tìm kiếm ứng với keyword đó
            return products_rslt

        if category != None:
            if len(products_rslt) == 1: # Nếu chỉ có 1 kết quả tìm kiếm
                return products_rslt if products_rslt[0].category_id == category else []
            products_rslt = [product for product in products_rslt if product.category_id == category]
        
        if maxPrice != None:
            if len(products_rslt) == 1: # Nếu chỉ có 1 kết quả tìm kiếm
                return products_rslt if products_rslt[0].price <= maxPrice else []
            products_rslt = [product for product in products_rslt if product.price <= maxPrice]
        
        if minPrice != None:
            if len(products_rslt) == 1: # Nếu chỉ có 1 kết quả tìm kiếm
                return products_rslt if products_rslt[0].price >= minPrice else []
            products_rslt = [product for product in products_rslt if products_rslt >= minPrice]
        
        
        # sortBy có 3 giá trị gồm 'time', 'sell', 'price'.
        # sortBy = time -> sản phẩm mới nhất
        if sortBy == 'time':
            products_rslt.sort(key = lambda x: x.publishing_year, reverse = True)

        # sortBy = sell -> sản phẩm mua nhiều nhất
        if sortBy == 'sell':
            pass
        
        # sortBy = price -> sản phẩm có giá từ thấp đến cao hoặc ngược lại
        # order có giá trị là 'asc'/'desc' ~ 'tăng/giảm'
        if sortBy == 'price':
            products_rslt.sort(key = lambda x: x.price, reverse = (order=='desc'))

        return products_rslt
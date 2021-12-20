from models.Product import Product
from repositories.UserRepository import UserRepository
from repositories.CategoryRepository import CategoryRepository
from repositories.StoreRepository import StoreRepository
from repositories.ProductRepository import ProductRepository
from repositories.OrderDetailRepository import OrderDetailRepository
from repositories.OrderProductRepository import OrderProductRepository
from models.Store import Store
from models.User import User
from models.Category import Category
from models.Province import Province
from models.OrderDetail import OrderDetail
from models.OrderProduct import OrderProduct
from peewee import *


dict1 = {"username": "catcat", "password": "12345678", "name": "WhoIsCatLover", "dob": "1991-02-12", "phone": "199123", "email": "catlover12@gmail.com", "avt_link": "https://i.pinimg.com/736x/21/2d/12/212d12e421963f8a66f95aece1182069.jpg?fbclid=IwAR3q_BfvC0p6Wif4XOIZ7YgUdDKS4mB8Z1uBi8pGyR33zYA8L-LEOxA37hg"}
dict2 = {"username": "ThebOOk", "password": "122323", "name": "TheBook", "dob": "1989-07-18", "phone": "190833", "email": "thebook@gmail.com", "avt_link": "https://i.pinimg.com/736x/21/2d/12/212d12e421963f8a66f95aece1182069.jpg?fbclid=IwAR3q_BfvC0p6Wif4XOIZ7YgUdDKS4mB8Z1uBi8pGyR33zYA8L-LEOxA37hg"}
user = dict1

catedict_1 = {"name": "Trinh thám"}
catedict_2 = {"name": "Ngoại văn"}
catedict_3 = {"name": "Khoa học"}
catedict_4 = {"name": "Truyện tranh"}
cate = catedict_4

storedict_1 = {"name": "BookS", "phone": "2342434", "email": "book@gmail.com", "rating": "0", "description": "Xin chào chúng tôi là BookS"}
storedict_2 = {"name": "CatCatBook", "phone": "1992405", "email": "cat@gmail.com", "rating": "0", "description": "Xin chào chúng tôi là CatCatBook"}
storedict_3 = {"name": "HahaVui", "owner_id": "5","phone": "1992405", "email": "hhVui@gmail.com", "rating": "0", "description": "Xin chào chúng tôi là HahaVui"}
store = storedict_3

#print(StoreRepository.createByUserId(store))

product_1 = {"name": "Trời xanh", "rating": "2", "description": "Cuốn sách kể về..", "detail": "ISO9800", "author": "Lê Văn Tèo", "number_of_pages": "157", "publishing_year": "2020-10-01", "publisher": "ProB", "cover_image": "link", "quantity": "20", "price": "250000"}
product_2 = {"name": "Cá vàng", "rating": "2", "description": "Cuốn sách kể về..", "detail": "ISO9800", "author": "Lê Văn Tèo", "number_of_pages": "157", "publishing_year": "2021-08-19", "publisher": "ProB", "cover_image": "link", "quantity": "20", "price": "250000"}
product_3 = {"name": "Hải âu", "rating": "2", "description": "Cuốn sách kể về..", "detail": "ISO9800", "author": "Lê Văn Tèo", "number_of_pages": "157", "publishing_year": "2010-02-05", "publisher": "ProB", "cover_image": "link", "quantity": "20", "price": "250000"}

product = product_1

#print(ProductRepository.create(4,"Văn học", product))
#print(ProductRepository.deleteById(2))
#print(ProductRepository.getByName("Trời xanh"))


order_1 = {"status": "1", "total_cost": "125000", "recipient_name": "Vũ Minh Tí", "recipient_phone": "1223342", "recipient_address": "134 ABC"}
order_2 = {"status": "1", "total_cost": "125000", "recipient_name": "Trần A", "recipient_phone": "1223342", "recipient_address": "250 XYZ"}
order_3 = {"status": "1", "total_cost": "125000", "recipient_name": "Nguyễn Văn Tèo", "recipient_phone": "1223342", "recipient_address": "19 LKC"}
order_4 = {"status": "1", "total_cost": "125000", "recipient_name": "Hồ Xuân M", "recipient_phone": "1223342", "recipient_address": "123F KSD"}
order_5 = {"status": "1", "total_cost": "125000", "recipient_name": "Lê Anh K", "recipient_phone": "1223342", "recipient_address": "20 MCV"}
order = order_1

order_pro_1 = {"quantity": "2"}
order_pro_2 = {"quantity": "1"}
order_pro_3 = {"quantity": "3"}
order_pro_4 = {"quantity": "1"}
order_pro = order_pro_1

#print(OrderDetailRepository.saveCreate(2,1,1,1,order))

#a = Product.select(Product, fn.SUM(OrderProduct.quantity).alias('sum')).join(OrderProduct).group_by(OrderProduct.product_id).order_by(fn.SUM(OrderProduct.quantity).desc()).offset(0).limit(2)

#for i in a:
    #print(i.name, i.id, i.sum)


print(UserRepository.deleteFromDB())


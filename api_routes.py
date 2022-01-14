from fastapi import APIRouter
from controllers.AdminController import AdminController
from controllers.OrderController import OrderController
from controllers.ProductController import ProductController
from controllers.StoreController import StoreController
from controllers.UserController import UserController
from controllers.ProductController import ProductController
from controllers.StoreController import StoreController
from controllers.CartController import CartController
from controllers.AddressController import AddressController
from controllers.ImageController import ImageController


api = APIRouter(prefix="/api")

# include controller
api.include_router(UserController.router)
api.include_router(ProductController.router)
api.include_router(StoreController.router)
api.include_router(StoreController.router2)
api.include_router(OrderController.router)
api.include_router(CartController.router)
api.include_router(AddressController.router)
api.include_router(ImageController.router)
api.include_router(AdminController.router)
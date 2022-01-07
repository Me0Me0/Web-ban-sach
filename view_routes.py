from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import FileResponse
import configs

view = APIRouter()

# Homepage
@view.get("/",response_class=FileResponse)
def homepage():
    return "views/homepage/index.html"


@view.get("/home",response_class=FileResponse)
def homepage():
    return "views/homepage/index.html"


# User
user_router = APIRouter(prefix="/users")


@user_router.get('/signin', response_class=FileResponse)
def signin():
    return "./views/signin/signin.html"


@user_router.get('/signup', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)]) 
def signup():
    return "./views/signup/signup.html"


@staticmethod
@user_router.get('/forgot-password', response_class=FileResponse) 
def forgotPassword():
    return "./views/forgotPassword/forgot-password.html"


@staticmethod
@user_router.get('/reset-password/{token}',response_class=FileResponse)
def resetPassword(token):
    return "./views/forgotPassword/forgot-password-2.html"


@staticmethod
@user_router.get('/view-profile', response_class=FileResponse)
def viewProfile():
    return "./views/viewProfile/view-profile.html"


@staticmethod
@user_router.get('/change-profile', response_class=FileResponse)
def changeProfile():
    return "./views/changeProfile/change-profile.html"


@staticmethod
@user_router.get('/change-password', response_class=FileResponse)
def changePassword():
    return "./views/changePassword/change-password.html"


view.include_router(user_router)


# MyStore
mystore_router = APIRouter(prefix="/mystore")


@mystore_router.get('', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page():
    return "./views/storeViewSeller/index.html"


@mystore_router.get('/add-product', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page():
    return "./views/addProduct/index.html"


@mystore_router.get('/register', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystoreRegistration():
    return "./views/stroreRegistration/index.html"


@mystore_router.get('/view-details', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page():
    return "./views/storeDetails_ViewSeller/index.html"


@mystore_router.get('/edit-details', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page():
    return "./views/editStore/index.html"


view.include_router(mystore_router)


# Stores
store_router = APIRouter(prefix="/stores")


@store_router.get('/{store_id}', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def storePage():
    return "./views/storeViewCus/index.html"


@store_router.get('/{store_id}/details', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def storeDetails():
    return "./views/storeDetails_ViewCus/index.html"


view.include_router(store_router)


# Products
product_router = APIRouter(prefix="/products")


@product_router.get('/best-seller', response_class=FileResponse)
def getBestSeller():
    return "./views/bestSeller/index.html"

@product_router.get('/category', response_class=FileResponse)
def getCategory():
    return "./views/category/index.html"


@product_router.get('/new-product', response_class=FileResponse)
def getNewProduct():
    return "./views/newProduct/index.html"


@product_router.get('/{id}', response_class=FileResponse)
def getProductDetails():
    return "./views/productViewCustomer/index.html"


@product_router.get('/details-view-seller', response_class=FileResponse)
def getProductDetailsViewSeller():
    return "./views/productViewSeller/index.html"


@product_router.get('/edit-product', response_class=FileResponse)
def getProductDetails():
    return "./views/editProduct/index.html"


view.include_router(product_router)


# Cart
cart_router = APIRouter(prefix="/cart")


# Add view bellow
@cart_router.get('/', response_class=FileResponse)
def getCart():
    return "./views/cart/index.html"


view.include_router(cart_router)


# order
order_router = APIRouter(prefix="/orders")



view.include_router(order_router)
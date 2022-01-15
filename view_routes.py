from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import FileResponse
from configs.dependency import redirectView, AUTH, NOT_AUTH
import configs

view = APIRouter()

# Homepage
@view.get("/",response_class=FileResponse)
def homepage():
    return "views/homepage/index.html"


@view.get("/home",response_class=FileResponse)
def homepage():
    return "views/homepage/index.html"

# Admin
admin_router = APIRouter(prefix="/admin")


@admin_router.get('/signin', response_class=FileResponse)
def signin():
    return "./views/adminSignin/signin.html"


@admin_router.get('/users', response_class=FileResponse)
def viewUserList(_ = Depends(redirectView("/admin/signin", NOT_AUTH, 'admin'))):
    return "./views/listUser/index.html"


@admin_router.get('/users/{id}', response_class=FileResponse)
def viewUserDetails(_ = Depends(redirectView("/admin/signin", NOT_AUTH, 'admin'))):
    return "./views/adminViewUser/index.html"


@admin_router.get('', response_class=FileResponse)
def viewUserList(_ = Depends(redirectView("/admin/signin", NOT_AUTH, 'admin'))):
    return "./views/adminPage/index.html"


view.include_router(admin_router)


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
def viewProfile(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/viewProfile/view-profile.html"


@staticmethod
@user_router.get('/change-profile', response_class=FileResponse)
def changeProfile(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/changeProfile/change-profile.html"


@staticmethod
@user_router.get('/change-password', response_class=FileResponse)
def changePassword(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/changePassword/change-password.html"


view.include_router(user_router)


# MyStore
mystore_router = APIRouter(prefix="/mystore")


@mystore_router.get('', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/storeViewSeller/index.html"


@mystore_router.get('/add-product', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/addProduct/index.html"


@mystore_router.get('/register', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystoreRegistration(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/stroreRegistration/index.html"


@mystore_router.get('/view-details', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/storeDetails_ViewSeller/index.html"


@mystore_router.get('/edit-details', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/editStore/index.html"

@mystore_router.get('/statistic', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)])
def mystore_page(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/statistic/index.html"


@mystore_router.get('/orders', response_class=FileResponse)
def getMyStoreOrders(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/listOrder_ViewSeller/index.html"


@mystore_router.get('/orders/{id}', response_class=FileResponse) # id cua don hang
def getMyStoreOrdersDetails(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/orderDetails_ViewSeller/index.html"


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


@product_router.get('/category/{id}', response_class=FileResponse)
def getCategory():
    return "./views/category/index.html"


@product_router.get('/new-product', response_class=FileResponse)
def getNewProduct():
    return "./views/newProduct/index.html"


@product_router.get('/search-results', response_class=FileResponse)
def getNewProduct():
    return "./views/searchResults/index.html"


@product_router.get('/view-seller/{id}', response_class=FileResponse)
def getProductDetailsViewSeller():
    return "./views/productViewSeller/index.html"


@product_router.get('/edit-product/{id}', response_class=FileResponse)
def editProductDetails(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/editProduct/index.html"


@product_router.get('/{id}', response_class=FileResponse)
def getProductDetails():
    return "./views/productViewCustomer/index.html"


view.include_router(product_router)


# Cart
cart_router = APIRouter(prefix="/cart")


# Add view bellow
@cart_router.get('', response_class=FileResponse)
def getCart(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/cart/index.html"


view.include_router(cart_router)


# order
order_router = APIRouter(prefix="/orders")


@order_router.get('/', response_class=FileResponse)
def getOrders(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/listOrder_ViewCus/index.html"


@order_router.get('/{id}', response_class=FileResponse) # id cua hoa don
def getOrderDetails(_ = Depends(redirectView("/users/signin", NOT_AUTH))):
    return "./views/orderDetails_ViewCus/index.html"


view.include_router(order_router)

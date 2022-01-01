from controllers.OrderController import OrderController
from controllers.ProductController import ProductController
from controllers.StoreController import StoreController
from controllers.UserController import UserController
from controllers.ProductController import ProductController
from controllers.StoreController import StoreController
from controllers.CartController import CartController
from repositories.UserRepository import UserRepository
from schemas import user_schema
from configs.env import getEnv
from configs.db import get_db

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles

import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#static files
app.mount("/public", StaticFiles(directory="public"))

# include controller
app.include_router(UserController.router)
app.include_router(ProductController.router)
app.include_router(StoreController.router)
app.include_router(StoreController.router2)
app.include_router(OrderController.router)
app.include_router(CartController.router)


@app.get("/", response_model=List[user_schema.User],dependencies=[Depends(get_db)])
def read_users(skip: int = 0, limit: int = 100):
    # get a list of all user
    users = UserRepository.getAll(skip = 0, limit = 100)
    return users


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={
        'error': exc.detail
    }, status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

@app.on_event("startup")
async def startup_event():
    sentry_sdk.init(
        dsn=getEnv().SENTRY_DSN,
        environment=getEnv().SENTRY_ENV,
    )
    app.add_middleware(SentryAsgiMiddleware)


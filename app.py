from controllers.UserController import UserController
from repositories.UserRepository import UserRepository
from schemas import schema
import configs

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include controller
app.include_router(UserController.router)

@app.get("/", response_model=List[schema.User],dependencies=[Depends(configs.db.get_db)])
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

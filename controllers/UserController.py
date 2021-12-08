
from typing import List
from fastapi import APIRouter
from fastapi.params import Query
from fastapi.responses import Response
from configs.constant import DUPLICATION_ERROR
from schemas import user_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.UserService import UserService


class UserController:
    router = APIRouter(prefix='/users')

    @staticmethod
    @router.get('/signin', response_class=FileResponse)
    def signin():
        return "./views/signin/index.html"

    @staticmethod
    @router.get('/signup', response_class=FileResponse) 
    def signup():
        return "./views/signup/index.html"

    @staticmethod
    @router.post('/signup')
    def signup(payload: user_schema.UserCreate):
        try:
            id = UserService.signup(payload)
        except Exception as e:
            if e.args[0] == DUPLICATION_ERROR:
                raise HTTPException(409, detail=e.args[1])
            raise Exception(e)

        return { 
            "data": {
                "id": id
            }
        }

    @staticmethod
    @router.post('/signin')
    def signin(payload: user_schema.UserLogin, response: Response):
        token = UserService.signin(payload)
        if not token:
            raise HTTPException(401, detail="Unauthorized")

        response.set_cookie(key="token", value=token, max_age=24*60*60, httponly=True)
        return {
            "data": {
                "success": True
            }
        }

    @staticmethod
    @router.get('', response_model=List[user_schema.User])
    def getAll(limit: int = Query(10, gt=0), skip: int =Query(0, ge=0)):
        return UserService.getAll(skip, limit)

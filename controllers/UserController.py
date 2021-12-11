
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.responses import Response
import configs

from configs.constant import DUPLICATION_ERROR
from schemas import user_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.UserService import UserService


class UserController:
    router = APIRouter(prefix='/users')

    @staticmethod
    @router.get('/signin', response_class=FileResponse,dependencies=[Depends(configs.db.get_db)])
    def signin():
        return "./views/signin/index.html"

    @staticmethod
    @router.get('/signup', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)]) 
    def signup():
        return "./views/signup/index.html"

    @staticmethod
    @router.post('/signup', dependencies=[Depends(configs.db.get_db)])
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
    @router.post('/signin', dependencies=[Depends(configs.db.get_db)])
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
    @router.get('', response_model=List[user_schema.User],dependencies=[Depends(configs.db.get_db)])
    def getAll(limit: int = Query(10, gt=0), skip: int =Query(0, ge=0)):
        return UserService.getAll(skip, limit)

    @staticmethod
    @router.get('/details', response_model=user_schema.User,dependencies=[Depends(configs.db.get_db)])
    def getDetail():
        user = UserService.getById(id)
        if not user:
            raise HTTPException(404, detail="User not found")
        return user

    @staticmethod
    @router.get('/{id}', response_model=user_schema.User,dependencies=[Depends(configs.db.get_db)])
    def getById(id: int):
        user = UserService.getById(id)
        if not user:
            raise HTTPException(404, detail="User not found")
        return user


    



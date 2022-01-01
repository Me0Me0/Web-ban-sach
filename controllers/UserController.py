from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.responses import Response
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR
from configs.dependency import getUser
from schemas import user_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.UserService import UserService
from services.EmailService import EmailService

class UserController:
    router = APIRouter(prefix='/users')


    @staticmethod
    @router.get('/signin', response_class=FileResponse,dependencies=[Depends(configs.db.get_db)])
    def signin():
        return "./views/signin/signin.html"


    @staticmethod
    @router.get('/signup', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)]) 
    def signup():
        return "./views/signup/signup.html"

    @staticmethod
    @router.get('/signout', response_class=FileResponse, dependencies=[Depends(configs.db.get_db)]) 
    def signup():
        return "./views/index.html"

    @staticmethod
    @router.get('/forgot-password', response_class=FileResponse) 
    def forgotPassword():
        return "./views/forgotPassword/forgot-password.html"

    @staticmethod
    @router.get('/home', response_class=FileResponse)
    def index():
        return "./views/homepage/index.html"

    @staticmethod
    @router.get('/view-profile', response_class=FileResponse)
    def viewProfile():
        return "./views/viewProfile/view-profile.html"

    @staticmethod
    @router.get('/change-profile', response_class=FileResponse)
    def changeProfile():
        return "./views/changeProfile/change-profile.html"

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
    def getDetail(currentUser = Depends(getUser)):
        user = UserService.getById(currentUser['id'])
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

    
    @staticmethod
    @router.put('/details', dependencies=[Depends(configs.db.get_db)])
    def update(payload: user_schema.UserUpdate, currentUser = Depends(getUser)):
        try:
            UserService.update(currentUser['id'], payload)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(404, detail=e.args[1])
            raise Exception(e)
            
        return {
            "data": {
                "success": True
            }
        }


    @staticmethod
    @router.post('/forgot-password')
    def forgetPassword(payload: user_schema.forgetPassword):
        try:
            user_email,user_name,token = UserService.forgetPassword(payload)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(404, detail=e.args[1])
            raise Exception(e)

        validated_link = './users/reset-password/' + token
        response = EmailService.sendEmail(user_email, user_name, validated_link)

        return {
            "data":{
                "status_code: " + str(response[0]),
                "message: " + str(response[1])
            }
        }


    @staticmethod
    @router.get('/forgot-password',response_class=FileResponse,dependencies=[Depends(configs.db.get_db)])
    def getInterface():
        return "./views/forgotPassword/forgot-password.html" 


    @staticmethod
    @router.post('/reset-password/{token}')
    def resetPassword(token: str, payload: user_schema.resetPassword):
        try:
            UserService.resetPassword(token, payload.password)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(404, detail=e.args[1])
            raise Exception(e)
        
        return {
            "data": {
                "success": True
            }
        }

      
    @staticmethod
    @router.get('/reset-password/{token}',response_class=FileResponse)
    def getInterface(token):
        return "./views/forgotPassword/forgot-password-2.html"

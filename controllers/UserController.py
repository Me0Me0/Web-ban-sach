from typing import List
from fastapi import APIRouter
from fastapi import responses
from fastapi.params import Depends, Query
from fastapi.responses import Response, RedirectResponse
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR, FORBIDDEN_ERROR, NOT_ACCEPTABLE_ERROR
from configs.dependency import getUser
from schemas import user_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

from services.UserService import UserService
from services.EmailService import EmailService

class UserController:
    router = APIRouter(prefix='/users')

    @staticmethod
    @router.get('/signout', dependencies=[Depends(configs.db.get_db)]) 
    def signout(response: Response):
        response.set_cookie('token', '', expires=0)
        response.set_cookie('loggedin', '', expires=0)
        response.headers['Location'] = '/'
        response.status_code = 307
        return response


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
        response.set_cookie(key="loggedin", value="true", max_age=24*60*60, httponly=False)
        return {
            "data": {
                "success": True
            }
        }


    @staticmethod
    @router.get('', response_model=List[user_schema.User],dependencies=[Depends(configs.db.get_db)])
    def getAll(limit: int = Query(10, gt=0), skip: int = Query(0, ge=0)):
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
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == 409:
                raise HTTPException(e.args[0], detail=e.args[1])
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

        validated_link = 'http://localhost:3000/users/reset-password/' + token
        response = EmailService.sendEmail(user_email, user_name, validated_link)

        return {
            "data": {
                "status_code": response[0],
                "message": response[1]
            }
        }


    @staticmethod
    @router.post('/reset-password/{token}')
    def resetPassword(token: str, payload: user_schema.resetPassword):
        try:
            UserService.resetPassword(token, payload.password)
        except Exception as e:
            if e.args[0] == NOT_ACCEPTABLE_ERROR:
                raise HTTPException(406, detail=e.args[1])
            raise Exception(e)
        
        return {
            "data": {
                "success": True
            }
        }

      
    @staticmethod
    @router.post('/change-password')
    def changePassword(payload: user_schema.changePassword, currentUser = Depends(getUser)):
        try:
            UserService.changePassword(currentUser['id'], payload.old_password, payload.new_password)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == FORBIDDEN_ERROR:
                raise HTTPException(e.args[0], detail=e.args[1])
            raise Exception(e)
        
        return {
            "data": {
                "success": True
            }
        }

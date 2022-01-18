from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.responses import Response
from fastapi.exceptions import HTTPException
from configs.constant import NOT_FOUND_ERROR
import configs
from schemas.admin_schema import AdminLogin
from schemas.user_schema import User
from services.AdminService import AdminService
from services.UserService import UserService
from configs.dependency import getAdmin

class AdminController:
    router = APIRouter(prefix='/admin')


    @staticmethod
    @router.post('/signin', dependencies=[Depends(configs.db.get_db)])
    def signin(payload: AdminLogin, response: Response):
        token = AdminService.signin(payload)
        if not token:
            raise HTTPException(401, detail="Unauthorized")

        response.set_cookie(key="token_admin", value=token, max_age=24*60*60, httponly=True)
        response.set_cookie(key="loggedin_admin", value="true", max_age=24*60*60, httponly=False)
        return {
            "data": {
                "success": True
            }
        }


    @staticmethod
    @router.get('/signout', dependencies=[Depends(configs.db.get_db)]) 
    def signout(response: Response, _ = Depends(getAdmin)):
        response.set_cookie('token_admin', '', expires=0)
        response.set_cookie('loggedin_admin', '', expires=0)
        response.headers['Location'] = '/admin/signin'
        response.status_code = 307
        return response


    @staticmethod
    @router.get('/users/{id}', response_model=User,dependencies=[Depends(configs.db.get_db)])
    def getDetail(id: int, _ = Depends(getAdmin)):
        user = AdminService.getUserDetail(id)
        if not user:
            raise HTTPException(404, detail="User not found")
        return user


    @staticmethod
    @router.get('/users', response_model=List[User],dependencies=[Depends(configs.db.get_db)])
    def getAll(limit: int = Query(10, gt=0), skip: int = Query(0, ge=0), _ = Depends(getAdmin)):
        return UserService.getAll(skip, limit)


    @staticmethod
    @router.delete('/users/{id}', dependencies=[Depends(configs.db.get_db)])
    def deleteUser(id: int, _ = Depends(getAdmin)):
        try:
            id = AdminService.deleteUser(id)
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR:
                raise HTTPException(404, detail=e.args[1])
            raise Exception(e)

        return { 
            "data": {
                "success": True
            }
        }



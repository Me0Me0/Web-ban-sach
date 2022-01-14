import bcrypt
import jwt
from datetime import datetime
from configs.env import getEnv
from repositories.AdminRepository import AdminRepository
from services.UserService import UserService
from schemas.admin_schema import AdminLogin

JWT_SECRET = getEnv().JWT_SECRET

class AdminService:


    @classmethod
    def signin(cls, payload: AdminLogin):
        adminDict = payload.__dict__

        # check username & password existence
        admin = AdminRepository.getByName(adminDict['username'])
        if not admin or not bcrypt.checkpw(adminDict['password'].encode(), admin['password'].encode()):
            return None
        
        # generate jwt token
        jwtPayload = {
            "id": admin["id"],
            "username": admin["username"],
            "role": "admin",
            "exp": int(datetime.now().timestamp()) + 24 * 60 * 60
        }
        token = jwt.encode(jwtPayload, JWT_SECRET)

        return token


    @classmethod
    def getAllAccount(cls, skip: int = 0, limit: int = 100):
        return UserService.getAll(skip, limit)


    @classmethod
    def getUserDetail(cls, id):
        return UserService.getById(id,True)


    @classmethod
    def deleteUser(cls, id: int):
        return UserService.deleteById(id)
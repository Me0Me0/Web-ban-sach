import bcrypt
import jwt

from datetime import datetime
from repositories.UserRepository import UserRepository
from schemas import user_schema
from fastapi.exceptions import HTTPException
from configs.constant import DEFAULT_AVT
from configs.env import getEnv
from services.CartService import CartService
from services.StoreService import StoreService

JWT_SECRET = getEnv().JWT_SECRET

class UserService:

    @classmethod
    def signup(cls, payload: user_schema.UserCreate):
        userDict = payload.__dict__
        userDict['avt_link'] = DEFAULT_AVT

        #hash password with bcrypt
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(userDict['password'].encode(), salt)
        userDict['password'] = hashed

        id = UserRepository.create(userDict)
        CartService.createCart(id)
        StoreService.registerStore(id)

        return id


    @classmethod
    def signin(cls, payload: user_schema.UserLogin):
        userDict = payload.__dict__

        # check username & password existence
        user = UserRepository.getByUsername(userDict['username'])
        if not user or not bcrypt.checkpw(userDict['password'].encode(), user.password.encode()):
            return None
        
        # generate jwt token
        jwtPayload = {
            "id": user.id,
            "username": user.username,
            "role": "member",
            "exp": int(datetime.now().timestamp()) + 24 * 60 * 60
        }
        token = jwt.encode(jwtPayload, JWT_SECRET)

        return token


    @classmethod
    def getAll(cls, skip: int = 0, limit: int = 100):
        return UserRepository.getAll(skip, limit)


    @classmethod
    def getById(cls, id, include_deleted: bool = False):
        return UserRepository.getById(id)

    
    @classmethod
    def update(cls, id, payload):
        try:
            return UserRepository.update(id, payload.__dict__)
        except Exception as e:
            raise Exception(409, "Duplicated email")
        


    @classmethod
    def getByUsername(cls, payload):
        return UserRepository.getByUsername(payload.username)


    @classmethod
    def forgetPassword(cls, payload: user_schema.forgetPassword):
        # check username existence
        user = UserRepository.getByUsername(payload.username)
        if not user:
            return None

        # generate jwt token
        jwtPayload = {
            "id": user.id,
            "exp": int(datetime.now().timestamp()) + 60
        }
        token = jwt.encode(jwtPayload, JWT_SECRET)
        return [user.email,user.name,token]


    @classmethod
    def resetPassword(cls, token_id, password):
        try:
            user = jwt.decode(token_id, JWT_SECRET, algorithms=["HS256"])
        except:
            raise Exception(406, 'Khong decode duoc!')
        
        # hash password with bcrypt
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(password.encode(), salt)
        
        return UserRepository.updatePassword(user['id'], hashed)


    @classmethod
    def changePassword(cls, user_id, old_password, new_password):
        user = UserRepository.getById(user_id)
        if not user or not bcrypt.checkpw(old_password.encode(), user.password.encode()):
            raise Exception(403, 'Sai mat khau!')
        
        # hash password with bcrypt
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(new_password.encode(), salt)

        return UserRepository.updatePassword(user_id, hashed)


    @classmethod
    def deleteUser(cls, id: int):
        return UserRepository.deleteById(id)
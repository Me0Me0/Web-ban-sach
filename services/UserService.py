import bcrypt
import jwt

from datetime import datetime
from repositories.UserRepository import UserRepository
from schemas import schema
from configs.constant import DEFAULT_AVT


class UserService:

    @classmethod
    def signup(cls, payload: schema.UserCreate):
        userDict = payload.__dict__
        userDict['avt_link'] = DEFAULT_AVT

        #hash password with bcrypt
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(userDict['password'].encode(), salt)
        userDict['password'] = hashed

        return UserRepository.create(payload.__dict__)

    @classmethod
    def signin(cls, payload: schema.UserLogin):
        userDict = payload.__dict__

        # check username & password existence
        user = UserRepository.getByUsername(userDict['username'])
        if not user or not bcrypt.checkpw(userDict['password'].encode(), user.password.encode()):
            return None
        
        # generate jwt token
        jwtPayload = {
            "id": user.id,
            "username": user.username,
            "exp": int(datetime.now().timestamp()) + 24 * 60 * 60
        }
        token = jwt.encode(jwtPayload, "secret")

        return token

    @classmethod
    def getAll(cls, skip, limit):
        return UserRepository.getAll(skip, limit)

       
import bcrypt
import jwt

from datetime import datetime
from repositories.UserRepository import UserRepository
from schemas import user_schema
from configs.constant import DEFAULT_AVT, JWT_SECRET


class UserService:

    @classmethod
    def signup(cls, payload: user_schema.UserCreate):
        userDict = payload.__dict__
        userDict['avt_link'] = DEFAULT_AVT

        #hash password with bcrypt
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(userDict['password'].encode(), salt)
        userDict['password'] = hashed

        return UserRepository.create(payload.__dict__)


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
            "exp": int(datetime.now().timestamp()) + 24 * 60 * 60
        }
        token = jwt.encode(jwtPayload, JWT_SECRET)

        return token


    @classmethod
    def getAll(cls, skip, limit):
        return UserRepository.getAll(skip, limit)


    @classmethod
    def getById(cls, id):
        return UserRepository.getById(id)

    
    @classmethod
    def update(cls, id, payload):
        return UserRepository.update(id, payload.__dict__)


    
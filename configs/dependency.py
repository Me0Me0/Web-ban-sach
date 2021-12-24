from fastapi.exceptions import HTTPException
import jwt
from fastapi import Request
from configs.constant import JWT_SECRET


def getUser(req: Request):
    try:
        currentUser = jwt.decode(req.cookies.get('token', ''), JWT_SECRET, algorithms=['HS256'])
    except:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return currentUser


def getStore(req: Request):
    try:
        currentStore = jwt.decode(req.cookies.get('token', ''), JWT_SECRET, algorithms=['HS256'])
    except:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return currentStore

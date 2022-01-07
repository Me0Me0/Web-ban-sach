from fastapi.exceptions import HTTPException
import jwt
from fastapi import Request
from configs.env import getEnv


def getUser(req: Request):
    try:
        currentUser = jwt.decode(req.cookies.get('token', ''), getEnv().JWT_SECRET, algorithms=['HS256'])
    except:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return currentUser

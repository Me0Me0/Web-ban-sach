from fastapi.exceptions import HTTPException
import jwt
from fastapi import Request, Response
from configs.env import getEnv


def getUser(req: Request):
    try:
        currentUser = jwt.decode(req.cookies.get('token', ''), getEnv().JWT_SECRET, algorithms=['HS256'])
        if currentUser['role'] != 'member':
            raise Exception()
    except:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return currentUser


def getAdmin(req: Request):
    try:
        currentUser = jwt.decode(req.cookies.get('token', ''), getEnv().JWT_SECRET, algorithms=['HS256'])
        if currentUser['role'] != 'admin':
            raise Exception()
    except:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return currentUser


NOT_AUTH = 1
AUTH = 2
def redirectView(path, when):
    def anonymous(req: Request, res: Response):
        try:
            currentUser = jwt.decode(req.cookies.get('token', ''), getEnv().JWT_SECRET, algorithms=['HS256'])
        except:
            currentUser = None

        if (when == NOT_AUTH and currentUser is None) or (when == AUTH and currentUser is not None):
            res.headers['Location'] = path
            res.status_code = 307
            return res
        
        return None
        
    return anonymous

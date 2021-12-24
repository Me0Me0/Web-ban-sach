from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from starlette.responses import FileResponse
import configs
from configs.constant import NOT_FOUND_ERROR, DUPLICATION_ERROR
from configs.dependency import getUser
from services.StoreService import StoreService

class StoreController:
    router = APIRouter(prefix='/stores')
    
    
    # Handler store operation from owner
    router2 = APIRouter(prefix='/mystore')

    @staticmethod
    @router2.get('/', response_class=FileResponse)
    def mystore_page():
        pass


    @staticmethod
    @router2.get('/details', dependencies=[Depends(configs.db.get_db)])
    def storeDetail(user = Depends(getUser)):
        try:
            store = StoreService.getOwnStore(user['id'])
        except Exception as e:
            if e.args[0] == 404:
                raise HTTPException(status_code=404, detail=e.args[1])
            raise Exception(e)
        return store

    
    @staticmethod
    @router2.post('/register')
    def registerStore(user = Depends(getUser)):
        try:
            store_id = StoreService.registerStore(user['id'])
        except Exception as e:
            if e.args[0] == NOT_FOUND_ERROR or e.args[0] == DUPLICATION_ERROR:
                raise HTTPException(status_code=e.args[0], detail=e.args[1])
            raise Exception(e)

        return {
            "id": store_id
        }


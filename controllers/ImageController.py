from fastapi.exceptions import HTTPException
from fastapi import Depends, File, APIRouter
from services.ImageService import ImageService
from configs.dependency import getUser

class ImageController:
    router = APIRouter(prefix='/images')

    @staticmethod
    @router.post("/upload")
    def upload(file: bytes = File(...), _ = Depends(getUser)):
        try:
            url = ImageService.upload(file)
        except:
            raise HTTPException(status_code=403, detail="Forbidden")

        return {
            "url": url
        }

        
        
from fastapi import File, APIRouter
from services.ImageService import ImageService

class ImageController:
    router = APIRouter(prefix='/images')

    @staticmethod
    @router.post("/upload")
    def upload(file: bytes = File(...)):
        url = ImageService.upload(file)
        return {
            "url": url
        }

        
        
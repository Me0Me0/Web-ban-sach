import requests
from configs.env import getEnv

class ImageService:

    @classmethod
    def upload(cls, file: bytes):
        clientID = getEnv().IMGUR_CLIENT_ID 
        headers = {
            'Authorization': f'Client-ID {clientID}'
        }
        files = [('image', file)]
        r = requests.post('https://api.imgur.com/3/upload', headers=headers, files=files)

        return r.json()['data']['link']


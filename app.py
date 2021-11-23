from repositories.UserRepository import UserRepository
import configs

from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# static files
app.mount("/public", StaticFiles(directory="public"))

@app.get("/", dependencies=[Depends(configs.db.get_db)])
def read_users():
    # get a list of all user
    users = UserRepository.getAll()

    return users[0]

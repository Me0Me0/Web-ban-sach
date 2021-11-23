from repositories.UserRepository import UserRepository
from schemas import schema
import configs

from typing import List
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

@app.get("/", response_model=List[schema.User],dependencies=[Depends(configs.db.get_db)])
def read_users(skip: int = 0, limit: int = 100):
    # get a list of all user
    users = UserRepository.getAll(skip = 0, limit = 100)

    return users

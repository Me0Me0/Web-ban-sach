from pydantic import BaseModel
from pydantic.types import constr

class AdminLogin(BaseModel):
    username: str
    password: constr(min_length=8)
from schemas.schema import PeeweeGetterDict

from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import constr
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: constr(min_length=8)
    name: str
    dob: date
    phone: int
    email: EmailStr


class UserLogin(BaseModel):
    username: str
    password: constr(min_length=8)


class User(BaseModel):
    id: int
    username: str
    name: str
    dob: date
    phone: int
    email: str
    avt_link: str
    
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
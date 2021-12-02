from typing import Any, List, Optional

import peewee
from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import constr
from pydantic.utils import GetterDict
from datetime import date


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


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
    # password: str
    name: str
    dob: date
    # address= str
    phone: int
    email: str
    avt_link: str
    
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
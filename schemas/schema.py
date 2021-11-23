from typing import Any, List, Optional

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict
from datetime import date


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class User(BaseModel):
    id: int
    username: str
    password: str
    name: str
    dob: date
    address= str
    phone= int
    email= int
    avt_link= int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
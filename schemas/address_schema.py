from peewee import FieldAlias
from pydantic import BaseModel, Field
from schemas.schema import PeeweeGetterDict
from schemas.user_schema import User


class Province(BaseModel):
    id: int
    name: str = Field(alias="_name")
    code: str = Field(alias="_code")

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class District(BaseModel):
    id: int
    name: str = Field(alias="_name")
    prefix: str = Field(alias="_prefix")
    province_id: int = Field(alias="_province_id")

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class Ward(BaseModel):
    id: int
    name: str = Field(alias="_name")
    prefix: str = Field(alias="_prefix")
    province_id: int = Field(alias="_province_id")
    district_id: int = Field(alias="_district_id")

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
from schemas.schema import PeeweeGetterDict

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
from pydantic import BaseModel, Field
from schemas.schema import PeeweeGetterDict
from schemas.user_schema import User


class Cart(BaseModel):
    id: int
    owner_id: User = Field(None)


    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
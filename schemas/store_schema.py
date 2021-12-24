from schemas.schema import PeeweeGetterDict
from schemas.user_schema import User

from pydantic import BaseModel, Field



class Store(BaseModel):
    id: int
    name: str
    owner_id: User = Field(None)
    phone: int
    email: str
    rating: float
    description: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
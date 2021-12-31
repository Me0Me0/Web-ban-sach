from pydantic import BaseModel, Field
from schemas.schema import PeeweeGetterDict
from schemas.user_schema import User

class Order(BaseModel):
    order_id: int
    product_id: int
    quantity: int 

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
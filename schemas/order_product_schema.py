from typing import List
from pydantic import BaseModel, Field
from schemas.schema import PeeweeGetterDict
from schemas.order_schema import OrderDetail
from schemas.product_schema import Product, ProductOrderDisplay

class OrderProduct(BaseModel):
    order_id: OrderDetail = Field(None)
    product_id: Product = Field(None)
    quantity: int 

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class OrderProductDisplay(BaseModel):
    product_id: ProductOrderDisplay = Field(None)
    quantity: int 

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

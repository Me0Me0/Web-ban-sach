from typing import List
from pydantic import BaseModel, Field
from schemas.schema import PeeweeGetterDict
from schemas.user_schema import User
from schemas.address_schema import Province, District, Ward
from schemas.product_schema import Product


class OrderProduct(BaseModel):
    product_id: Product
    quantity: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class OrderDetail(BaseModel):
    id: int

    status: int
    total_cost: float

    recipient_name: str
    recipient_phone: int
    recipient_address: str
    
    province_id: Province
    district_id: District
    ward_id: Ward

    order_products: List[OrderProduct]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class OrderCreationProduct(BaseModel):
    product_id: int
    quantity: int


class OrderCreation(BaseModel):
    recipient_name: str
    recipient_phone: int
    recipient_address: str
    province_id: int
    district_id: int
    ward_id: int
    products: List[OrderCreationProduct]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
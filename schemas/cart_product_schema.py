from schemas.schema import PeeweeGetterDict
from schemas.product_schema import Product
from schemas.cart_schema import Cart

from pydantic import BaseModel, Field


class CartProduct(BaseModel):
    cart_id: Cart = Field(None)
    product_id: Product = Field(None)
    quantity: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class CartProductQuantityUpdate(BaseModel):
    quantity: int = Field(..., gt=0)
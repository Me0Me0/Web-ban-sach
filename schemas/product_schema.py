from schemas.schema import PeeweeGetterDict
from schemas.category_schema import Category
from schemas.store_schema import Store

from pydantic import BaseModel, Field
from datetime import date

class Product(BaseModel):
    id: int
    name: str
    cate_id: Category = Field(None)
    #rating: float
    description: str
    detail: str
    author: str
    number_of_pages: int
    publishing_year: date
    publisher: str
    cover_image: str
    store_id: Store = Field(None)
    quantity: int
    price: float

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class ProductCreate(BaseModel):
    name: str
    cate_id: int
    description: str
    detail: str
    author: str
    number_of_pages: int
    publishing_year: date
    publisher: str
    quantity: int
    price: float


class ProductUpdate(BaseModel):
    name: str
    cate_id: int
    description: str
    detail: str
    author: str
    number_of_pages: int
    publishing_year: date
    publisher: str
    cover_image: str
    quantity: int
    price: float


class ProductUpdateCoverImage(BaseModel):
    image_link: str


class ProductUpdateImages(BaseModel):
    list_image_link: list


class ProductSell(Product):
    sum: int


class ProductOrderDisplay(BaseModel):
    id: int
    name: str
    price: float


    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
    
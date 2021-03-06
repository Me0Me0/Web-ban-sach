from typing import List, Any
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
    publishing_year: int
    publisher: str
    cover_image: str
    store_id: Store = Field(None)
    quantity: int
    price: float
    product_images: List[Any] = []

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class ProductCreate(BaseModel):
    name: str = Field(..., max_length=75)
    cate_id: int
    description: str = Field(..., max_length=30)
    detail: str
    author: str = Field(..., max_length=30)
    number_of_pages: int
    publishing_year: int
    image_links: List[str]
    cover_image: str
    publisher: str = Field(..., max_length=30)
    quantity: int
    price: float


class ProductUpdate(BaseModel):
    name: str = Field(..., max_length=75)
    cate_id: int
    description: str = Field(..., max_length=30)
    detail: str
    author: str = Field(..., max_length=30)
    number_of_pages: int
    publishing_year: int
    publisher: str = Field(..., max_length=30)
    cover_image: str
    quantity: int
    price: float


class ProductUpdateCoverImage(BaseModel):
    image_link: str


class ProductUpdateImage(BaseModel):
    id: int
    image_link: str


class ProductUpdateImages(BaseModel):
    list_image_link: List[ProductUpdateImage]


class ProductSell(Product):
    sum: int


class ProductBestSell(BaseModel):
    id: int
    name: str
    cate_id: Category = Field(None)
    author: str
    publishing_year: int
    cover_image: str
    price: float
    sum: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class ProductBestSellCate(BaseModel):
    cate_id: Category = Field(None)
    sum: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class ProductOrderDisplay(BaseModel):
    id: int
    name: str
    price: float


    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
    
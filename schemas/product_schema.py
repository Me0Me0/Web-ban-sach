from schemas.schema import PeeweeGetterDict
from schemas.category_schema import Category
from schemas.store_schema import Store

from pydantic import BaseModel, Field
from datetime import date

class Product(BaseModel):
    id: int
    name: str
    cate_id: Category = Field(None)
    rating: float
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
    category: str
<<<<<<< Updated upstream
    #cate_id: Category = Field(None)
    rating: float
=======
>>>>>>> Stashed changes
    description: str
    detail: str
    author: str
    number_of_pages: int
    publishing_year: date
    publisher: str
<<<<<<< Updated upstream
    #cover_image: str
=======
>>>>>>> Stashed changes
    quantity: int
    price: float


class ProductUpdate(BaseModel):
    name: str
    category: str
<<<<<<< Updated upstream
    #cate_id: Category = Field(None)
    rating: float
=======
>>>>>>> Stashed changes
    description: str
    detail: str
    author: str
    number_of_pages: int
    publishing_year: date
    publisher: str
    cover_image: str
    quantity: int
    price: float


class ProductSell(Product):
    sum: int
    
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import Response
import configs

from configs.constant import DUPLICATION_ERROR, NOT_FOUND_ERROR, FORBIDDEN_ERROR
from schemas import product_schema
from schemas import cart_schema
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from configs.dependency import getUser

from services.ProductService import ProductService
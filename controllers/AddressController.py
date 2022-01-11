from typing import List
from fastapi import APIRouter, Depends, HTTPException

from services.AddressService import AddressService
from schemas import address_schema
import configs


class AddressController:
    router = APIRouter(prefix="/address")

    @staticmethod
    @router.get("/provinces", response_model=List[address_schema.Province], dependencies=[Depends(configs.db.get_db)])
    def getProvinces():
        return AddressService.getProvinces()

    
    @staticmethod
    @router.get("/districts", response_model=List[address_schema.District], dependencies=[Depends(configs.db.get_db)])
    def getDistricts(province_id: int):
        return AddressService.getDistricts(province_id)

    
    @staticmethod
    @router.get("/wards", response_model=List[address_schema.Ward], dependencies=[Depends(configs.db.get_db)])
    def getWards(district_id: int):
        return AddressService.getWards(district_id)
from repositories.ProvinceRepository import ProvinceRepository
from repositories.DistrictRepository import DistrictRepository
from repositories.WardRepository import WardRepository

class AddressService:

    @classmethod
    def getProvinces(cls):
        return ProvinceRepository.getAll()

    
    @classmethod
    def getDistricts(cls, province_id):
        return DistrictRepository.getByProvince(province_id)

    
    @classmethod
    def getWards(cls, district_id):
        return WardRepository.getByDistrict(district_id)
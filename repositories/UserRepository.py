from models.User import User
from schemas import schema


class UserRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      records = User.select()
      result = []
      for record in records:
         person = {
            "id": record.id,
            "username": record.username,
            "password": record.password,
            "name": record.name.encode(),
            "dob": record.dob,
            "phone": record.phone,
            "email": record.email,
            "avt_link": record.avt_link
         } 
         result.append(person)
      #return result
      return list(User.select().offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):

      for record in User.select().where(User.id==id):
         person = {
            "id": record.id,
            "username": record.username,
            "password": record.password,
            "name": record.name.encode(),
            "dob": record.dob,
            "phone": record.phone,
            "email": record.email,
            "avt_link": record.avt_link
         } 

      #return person
      return User.filter(User.id == id).first()


   @classmethod
   def getPasswordById(cls,id) -> str:

      for record in User.select(User.password).where(User.id==id):
         result = record

      return result.password
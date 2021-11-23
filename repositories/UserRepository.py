from repositories.IRepository import IRepository
from models.User import User

class UserRepository(IRepository):

   @classmethod
   def getAll(cls):
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
      return result


   @classmethod
   def getById(cls, id):

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

      return person


   @classmethod
   def getUserNameByPassword(cls,pwd) -> str:

      for record in User.select(User.username).where(User.password==pwd):
         result = record

      return result.username


   @classmethod
   def getAvatarLink(cls,id) -> str:

      for record in User.select(User.avt_link).where(User.id==id):
         result = record

      return result.avt_link


   @classmethod
   def getPasswordById(cls,id) -> str:

      for record in User.select(User.password).where(User.id==id):
         result = record

      return result.password


   @classmethod
   def getPasswordByUsername(cls,name) -> str:

      for record in User.select(User.password).where(User.username==name):
         result = record

      return result.password


   @classmethod
   def getAllPassword(cls):
      result = []

      for record in User.select(User.password):
         result.append(record.password)

      return result
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
   def getByUsername(cls,username) -> str:
      result = None
      for record in User.select(User.password).where(User.username==username):
         result = record

      return result

   
   @classmethod
   def create(cls, userDict):
      try:
         return User.create(**userDict).id
      except Exception as e:
         if e.args[0] == 1062:
            field = "email"
            if "user.username" in e.args[1]:
               field = "username"
            raise Exception(409, { "field": field })
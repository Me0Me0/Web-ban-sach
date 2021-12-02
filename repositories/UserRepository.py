from peewee import *
from models.User import User


class UserRepository():

   @classmethod
   def getAll(cls, skip: int = 0, limit: int = 100):
      return list(User.select().offset(skip).limit(limit))


   @classmethod
   def getById(cls, id: int):
<<<<<<< Updated upstream

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
=======
      return list(User.select().where(User.id == id))

   
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


   @classmethod
   def deleteById(cls, id: int):
      try:
         delete_user = User.get_by_id(id)
      except:
         raise Exception(404, { "DELETE ERROR": "Can not find user with given id" })

      return delete_user.delete_instance()


   @classmethod
   def updatePassword(cls, id: int, passwd: str):
      try:
         update_user = User.get_by_id(id)
      except:
         raise Exception(404, { "UPDATE ERROR": "Can not find user with given id" })

      update_user.password = passwd
      return update_user.save()


   @classmethod
   def updateUsername(cls, id: int, usrname: str):
      try:
         update_user = User.get_by_id(id)
      except:
         raise Exception(404, { "UPDATE ERROR": "Can not find user with given id" })

      update_user.username = usrname
      return update_user.save()


   @classmethod
   def updatePhone(cls, id: int, number: int):
      try:
         update_user = User.get_by_id(id)
      except:
         raise Exception(404, { "UPDATE ERROR": "Can not find user with given id" })

      update_user.phone = number
      return update_user.save()


   @classmethod
   def updateAvatar(cls, id: int, link: str):
      try:
         update_user = User.get_by_id(id)
      except:
         raise Exception(404, { "UPDATE ERROR": "Can not find user with given id" })

      update_user.avt_link = link
      return update_user.save()

>>>>>>> Stashed changes

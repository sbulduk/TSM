from .IModel import IModel
from sqlalchemy import Column,String
import uuid
from sqlalchemy.orm import relationship
from argon2 import PasswordHasher

ph=PasswordHasher()

class User(IModel):
    __tablename__="Users"
    Id=Column(String(36),primary_key=True,default=lambda:str(uuid.uuid4()))
    UserName=Column(String(32),unique=True,nullable=False)
    Email=Column(String(64),unique=True,nullable=False)
    HashedPassword=Column(String(256),nullable=False)

    Roles=relationship("Role",secondary="UsersRoles",back_populates="Users")

    def SetPassword(self,password:str)->None:
        self.HashedPassword=ph.hash(password)

    def VerifyPassword(self,password:str)->bool:
        return ph.verify(self.HashedPassword,password)
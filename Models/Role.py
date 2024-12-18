from .IModel import IModel
from sqlalchemy import Column,String
from sqlalchemy.orm import relationship
import uuid

class Role(IModel):
    __tablename__="Roles"
    Id=Column(String(36),primary_key=True,default=lambda:str(uuid.uuid4()))
    Name=Column(String(32),unique=True,nullable=False)
    Description=Column(String(256))
    
    Users=relationship("User",secondary="UsersRoles",back_populates="Roles")
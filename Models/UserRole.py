from .IModel import IModel
from sqlalchemy import Column,String,ForeignKey

class UserRole(IModel):
    __tablename__="UsersRoles"
    UserId=Column(String(36),ForeignKey("Users.Id"),primary_key=True)
    RoleId=Column(String(36),ForeignKey("Roles.Id"),primary_key=True)
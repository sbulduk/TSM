from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from Models.User import User
from Models.Role import Role
from Models.UserRole import UserRole
from datetime import datetime,timezone,timedelta
from authlib.jose import jwt
from dynaconf import settings





class AuthService(object):
    def __init__(self,dbSession:Session)->None:
        self.dbSession=dbSession
        self.ph=PasswordHasher()

    def GenerateJWT(self,user:User):
        claims={
            "sub":str(user.Id),
            "exp":datetime.now(timezone.utc)+timedelta(hours=1),
            "roles":[role.Name for role in user.Roles]
        }
        jwt.encode({"alg":"HS256"},claims,settings.JWT_SECRET)

    def Authenticate(self,userName:str,password:str)->str:
        user=self.dbSession.query(User).filter(User.UserName==userName).first()
        if user and user.VerifyPassword(password):
            return self.GenerateJWT(user)

    def GetUserFromJWT(self,token:str)->User:
        claims=jwt.decode(token,settings.JWT_SECRET)
        

    def RequiresAuth(self,f):
        pass
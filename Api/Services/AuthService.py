from structlog import get_logger
from Middleware.Config import Config
from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from Models.User import User
from datetime import datetime,timezone,timedelta
from authlib.jose import jwt
import uuid

logger=get_logger()
config=Config.settings

class AuthService(object):
    def __init__(self,dbSession:Session)->None:
        self.dbSession=dbSession
        self.ph=PasswordHasher()

        self.secretKey=config["JWT"]["SecretKey"]
        self.algorithm=config["JWT"]["Algorithm"]
        self.tokenExpiration=config["JWT"]["TokenExpiration"]

        # self.secretKey=config.JWT.SecretKey
        # self.algorithm=config.JWT.Algorithm
        # self.tokenExpiration=config.JWT.TokenExpiration

    def GenerateJWT(self,user:User)->str:
        payload={
            "sub":str(user.Id),
            "username":user.UserName,
            "roles":[role.Name for role in user.Roles],
            "iat":datetime.now(timezone.utc),
            "exp":datetime.now(timezone.utc)+timedelta(minutes=self.tokenExpiration)
        }
        token=jwt.encode({"alg":self.algorithm},payload,self.secretKey)
        logger.debug("JWT generated",userName=user.UserName,roles=payload["roles"])
        return token.decode("utf-8")

    def DecodeJWT(self,token:str)->dict:
        payload=jwt.decode(token,self.secretKey)
        payload.validate()
        logger.debug("JWT decoded successfully",token=token)
        return payload
    
    def GetUserbyId(self,userId:str)->User:
        user=self.dbSession.query(User).filter(User.Id==userId).first()
        if not user:
            return None
        return user
    
    def Register(self,userName:str,email:str,password:str)->list[str]:
        user=User(Id=str(uuid.uuid4()),UserName=userName,Email=email)
        user.SetPassword(password)
        self.dbSession.add(user)
        self.dbSession.commit()
        logger.info("User registered",userId=user.Id)
        token=self.Login(userName,password)
        if token:
            return user.Id,token
        return None

    def Login(self,userName:str,password:str)->str:
        user=self.dbSession.query(User).filter(User.UserName==userName).first()
        if user and user.VerifyPassword(password):
            logger.info("Successfull login",userName=userName)
            return self.GenerateJWT(user)
        else:
            logger.info("Login failed",userName=userName)
            return None
        
    def Authorize(self,token:str,requiredRoles:list[str])->bool:
        payload=self.DecodeJWT(token)
        userRoles=payload.get("roles",[])
        authorized=any(role in requiredRoles for role in userRoles)
        logger.info(
            "Authorization check",
            token=token,
            requiredRoles=requiredRoles,
            authorized=authorized
        )
        return authorized

    def CheckUserRole(self,userId:str,roleName:str)->bool:
        hasRole=False
        user=self.dbSession.query(User).filter(User.Id==userId).first()
        if user:
            hasRole=any(role.Name==roleName for role in user.Roles)
            logger.debug("Role check",userId=userId,roleName=roleName,hasRole=hasRole)
        return hasRole
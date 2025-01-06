# from structlog import get_logger
from Middleware.Config import Config
from sqlalchemy.orm import Session
from Models.User import User

# logger=get_logger()
config=Config.settings

class UserService(object):
    def __init__(self,dbSession:Session)->None:
        self.dbSession=dbSession
    
    def GetUserbyId(self,userId:str)->User:
        user=self.dbSession.query(User).filter(User.Id==userId).first()
        if not user:
            return None
        return user
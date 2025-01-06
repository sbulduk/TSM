from structlog import get_logger
from sqlalchemy.orm import Session
from Models.User import User
from Models.Role import Role
from Models.UserRole import UserRole
from .AuthService import AuthService
from .RoleService import RoleService

logger=get_logger()

class UserRoleService(object):
    def __init__(self,dbSession:Session):
        self.dbSession=dbSession
    
    def GetUserRoles(self,userId:str)->list:
        userRoles=self.dbSession.query(UserRole).filter(UserRole.UserId==userId).all()
        roles=[self.dbSession.query()]

    def AddUserRole(self,userId:str,roleId:str)->bool:
        authService=AuthService(self.dbSession)
        roleService=RoleService(self.dbSession)

        user=authService.GetUserbyId(userId)
        role=roleService.GetRolebyId(roleId)

        if user and role:
            userRole=UserRole(UserId=userId,RoleId=roleId)
            self.dbSession.add(userRole)
            self.dbSession.commit()
            logger.info("User-Role added.",userId=userId,roleId=roleId)
            return True
        return False

    def DeleteUserRole(self,userId:str,roleId:str)->bool:
        userRole=self.dbSession.query(UserRole).filter(UserRole.UserId==userId,UserRole.RoleId==roleId).first()
        if userRole:
            self.dbSession.delete(userRole)
            self.dbSession.commit()
            logger.info("User-Role deleted: ",userId=userId,roleId=roleId)
            return True
        return False
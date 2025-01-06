from structlog import get_logger
from sqlalchemy.orm import Session
from Models.Role import Role
import uuid

logger=get_logger()

class RoleService(object):
    def __init__(self,dbSession:Session)->None:
        self.dbSession=dbSession

    def GetRolebyId(self,roleId:str)->Role:
        role=self.dbSession.query(Role).filter(Role.Id==roleId).first()
        if not role:
            return None
        return role

    def GetRoleList(self)->list[Role]:
        roles=self.dbSession.query(Role).all()
        return roles

    def AddRole(self,roleName:str,description:str=None)->str:
        role=Role(Id=str(uuid.uuid4()),Name=roleName,Description=description)
        self.dbSession.add(role)
        self.dbSession.commit()
        logger.info("Role added",roleId=role.Id)
        return role.Id

    def UpdateRole(self,roleId:str,roleName:str,description:str=None)->bool:
        role=self.GetRolebyId(roleId)
        if role:
            if roleName:
                role.Name=roleName
            if description:
                role.Description=description

            self.dbSession.commit()
            logger.info("Role updated: ",roleId=role.Id)
        else:
            return None

    def DeleteRole(self,roleId:str)->bool:
        role=self.GetRolebyId(roleId)
        if role:
            self.dbSession.delete(role)
            self.dbSession.commit()
            logger.info("Role deleted: ",roleId=roleId)
            return True
        return False
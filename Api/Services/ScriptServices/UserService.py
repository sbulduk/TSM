from .IScriptService import IScriptService
import os

class UserService(IScriptService):
    def __init__(self,remoteServer:str,userName:str,password:str):
        super().__init__(remoteServer,userName,password)
        currentDirectory=os.path.dirname(os.path.abspath(__file__))
        self.scriptPath=os.path.join(currentDirectory,"Scripts","UserHelper.ps1")
        self.className="UserHelper"

    def GetUserDetails(self,identity:str):
        return self.InvokePowerShellMethod(self.scriptPath,self.className,"GetUserDetails",params=[identity])

    def EnableUser(self,identity:str):
        return self.InvokePowerShellMethod(self.scriptPath,self.className,"EnableUser",identity)

    def DisableUser(self,identity:str):
        return self.InvokePowerShellMethod(self.scriptPath,self.className,"DisableUser",identity)

    def AddNewUser(self,name:str,samAccountName:str,displayName:str,initialPassword:str,email:str,ouPath:str):
        return self.InvokePowerShellMethod(
            self.scriptPath,
            self.className,
            "AddNewUser",
            name,
            samAccountName,
            displayName,
            initialPassword,
            email,
            ouPath,
        )
from abc import ABC
import subprocess
import json

class IScriptService(ABC):
    def __init__(self,remoteServer:str,userName:str,password:str)->None:
        self.remoteServer=remoteServer
        self.userName=userName
        self.password=password

    def InvokePowerShellMethod(self,scriptPath:str,className:str,methodName:str,params:list[str]=None)->str:
        # paramStr=", ".join(f"'{p}'" for p in params) if params else ""
        paramStr=", ".join(str(p) for p in params) if params else ""
        psCommand=f"""
            . "{scriptPath}"
            $instance=New-Object -TypeName "{className}" -ArgumentList "{self.remoteServer}","{self.userName}","{self.password}"
            $result=$instance.{methodName}("{paramStr}")
            $result
        """

        print(f"{psCommand}")

        response=subprocess.run(
            ["powershell","-Command",psCommand],
            capture_output=True,
            text=True
        )
        if response.returncode!=0:
            raise Exception(f"Error executing script: {response.stderr}")
        try:
            pass
            return json.loads(response.stdout)
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON output from PowerShell: {response.stdout}")

    # @abstractmethod
    # def Execute(self,*args,**kwargs):
    #     pass
from abc import ABC,abstractmethod
import winrm

class IScriptService(ABC):
    def __init__(self,remoteServer:str,userName:str,password:str)->None:
        self.remoteServer=remoteServer
        self.userName=userName
        self.password=password

    def InvokePowerShellMethod(self,scriptPath:str,className:str,methodName:str,*args:any):
        try:
            session=winrm.Session(self.remoteServer,auth=(self.userName,self.password),transport="ntlm")
            with open(scriptPath,"r") as scriptFile:
                script=scriptFile.read()
            params=" ".join([f"'{arg}'" for arg in args])
            # script=(
            #     f"Import-Module '{scriptPath}';"
            #     f"$instance=[{className}]::new('{self.remoteServer}','{self.userName}','{self.password}');"
            #     f"$result=$instance.{methodName}({params});"
            #     f"$result"
            # )

            # script=(
            #     f"Import Module '{scriptPath}';"
            #     f"$instance=New-Object -TypeName '{className}' -ArgumentList '{self.remoteServer}','{self.userName}','{self.password}';"
            #     f"$result=$instance.{methodName}({params});"
            #     f"$result"
            # )
            print("A")
            script=f"""
                Import-Module '{scriptPath}'
                $instance=New-Object -TypeName '{className}' -ArgumentList '{self.remoteServer}','{self.userName}','{self.password}'
                $result=$instance.{methodName}({params})
                $result 
            """
            print(f"{scriptPath}")
            print("B")
            print(f"{script}")
            print("C")

            response=session.run_ps(script)
            # Convert
            print("D")
            if response.status_code!=0:
                raise Exception(f"Error executing script: {response.std_err.decode()}")
            return response.std_out.decode()
        except Exception as e:
            raise RuntimeError(f"Failed to invoke PowerShell method: {str(e)}")
        

    # @abstractmethod
    # def Execute(self,*args,**kwargs):
    #     pass
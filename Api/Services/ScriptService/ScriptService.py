import subprocess

class ScriptService(object):
    def RunPowerShell(self,scriptPath:str,*args:object)->dict:
        try:
            command=["powershell","-ExecutionPolicy","Bypass","-File",scriptPath,*args]
            result=subprocess.run(command,capture_output=True,text=True,check=True)
            return {"success":True,"error":result.stderr,"success":True}
        except subprocess.CalledProcessError as e:
            return {"success":False,"output":e.stdout,"error":e.stderr}
import winrm

class ScriptService(object):
    def __init__(self,host:str,userName:str,password:str)->None:
        self.host=host
        self.session=winrm.Session(
            f"http://{host}:5985/wsman",
            auth=(userName,password),
            transport="ntlm"
        )

    def ExecutePowershell(self,script:str,args:list=None)->dict:
        if args:
            cmd=f"{script}"+" ".join([str(arg) for arg in args])
        else:
            cmd=script
        response=self.session.run_ps(cmd)
        return {
            "stdout":response.std_out.decode("latin-1").strip(),
            "stderr":response.std_err.decode("latin-1").strip(),
            "status_code":response.status_code
        }



    # def RunPowerShell(self,scriptPath:str,*args:object)->dict:
    #     try:
    #         command=["powershell","-ExecutionPolicy","Bypass","-File",scriptPath,*args]
    #         result=subprocess.run(command,capture_output=True,text=True,check=True)
    #         return {"success":True,"error":result.stderr,"success":True}
    #     except subprocess.CalledProcessError as e:
    #         return {"success":False,"output":e.stdout,"error":e.stderr}
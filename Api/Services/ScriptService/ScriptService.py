import winrm

class ScriptService(object):
    def __init__(self,host:str,userName:str,password:str)->None:
        self.host=host
        self.session=winrm.Session(
            f"http://{host}:5985/wsman",
            auth=(userName,password),
            transport="ntlm"
        )

    def ExecuteScript(self,script:str,params:dict=None)->dict:
        paramsStr=" ".join([f"-{key} {value}" for key,value in (params or {}).items()])
        command=f"{script} {paramsStr}"
        response=self.session.run_ps(command)
        return {
            "stdout":response.std_out.decode("latin-1").strip(),
            "stderr":response.std_err.decode("latin-1").strip(),
            "status_code":response.status_code
        }
    
    def InvokeClassMethod(self,className:str,methodName:str,params:dict=None)->dict:
        paramsStr=";".join([f"$params.add('{key}','{value}')" for key,value in (params or {}).items()])
        script=f"""
            $params=@{{}}
            {paramsStr}
            $remoteHelper=[RemoteHelper]::new("{self.host}","{self.session.auth[0]}","{self.session.auth[1]}")
            $result=$remoteHelper.RunMethod("{className}","{methodName}",$params)
            $result
        """
        return self.ExecuteScript(script)
    
    def RunScriptFile(self,filePath:str,params:dict=None)->dict:
        paramsStr=";".join([f"$params.Add('{key}','{value}')" for key,value in (params or {}).items()])
        script=f"""
            $params=@{{}}
            {paramsStr}
            $remoteHelper=[RemoteHelper]::new("{self.host}","{self.session.auth[0]}","{self.session.auth[1]}")
            $result=$remoteHelper.RunScriptFile("{filePath}",$params)
            $result
        """
        return self.ExecuteScript(script)


    # FIRST RUNNING SHELL SCRIPT!!!
    # def ExecutePowershellCommand(self,script:str,args:list=None)->dict:
    #     if args:
    #         cmd=f"{script}"+" ".join([str(arg) for arg in args])
    #     else:
    #         cmd=script
    #     response=self.session.run_ps(cmd)
    #     return {
    #         "stdout":response.std_out.decode("latin-1").strip(),
    #         "stderr":response.std_err.decode("latin-1").strip(),
    #         "status_code":response.status_code
    #     }

    # def RunPowerShell(self,scriptPath:str,*args:object)->dict:
    #     try:
    #         command=["powershell","-ExecutionPolicy","Bypass","-File",scriptPath,*args]
    #         result=subprocess.run(command,capture_output=True,text=True,check=True)
    #         return {"success":True,"error":result.stderr,"success":True}
    #     except subprocess.CalledProcessError as e:
    #         return {"success":False,"output":e.stdout,"error":e.stderr}
from flask import Blueprint,jsonify,request
from API.Services.ScriptService.ScriptService import ScriptService

ScriptBlueprint=Blueprint("ScriptBlueprint",__name__,url_prefix="/script")
scriptService=ScriptService("192.168.2.2","sbulduk","Sbulduk2024!")

@ScriptBlueprint.route("/executescript",methods=["GET"])
def ExecuteScript():
    scriptContent="Get-Process | Select-Object -First 5"
    try:
        result=scriptService.ExecuteScript(scriptContent)
        print("Standard Output:",result["stdout"])
        print("Standard Error:",result["stderr"])
        print("Exit Code:",result["status_code"])
        return jsonify({"success":True,"data":f"{result}"}),200
    except Exception as e:
        return({"success":False,"data":f"Check user credentials."}),400
    
@ScriptBlueprint.route("/invokeclassmethod",methods=["POST"])
def InvokeClassMethod():
    try:
        # TODO: Turn this static parameters into dynamic, to be read from json file!!!
        script=scriptService.InvokeClassMethod(
            className="ComputerHelper",
            methodName="CheckComputerExists",
            params={"computerName":"AS-TASKIN72"}
        )
        return jsonify({"success":True,"data":f"{script}"}),200
    except Exception as e:
        return jsonify({"success":False,"data":f"InvokeClassMethod Error: {e}"}),400
    
@ScriptBlueprint.route("/runscriptfile",methods=["POST"])
def RunScriptFile():
    try:
        filePath="..\\Services\\ScriptService\\Scripts\\ComputerHelper.ps1"
        params={"OUPath":"OU=Computers,DC=blahblah,DC=comblah"}
        script=scriptService.RunScriptFile(
            filePath=filePath,
            params=params
        )
        return jsonify({"success":True,"data":f"{script}"}),200
    except Exception as e:
        return jsonify({"success":False,"data":f"RunScriptFile Error: {e}"}),400
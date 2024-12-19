from flask import Blueprint,jsonify,request
from API.Services.ScriptService.ScriptService import ScriptService

ScriptBlueprint=Blueprint("ScriptBlueprint",__name__,url_prefix="/script")
scriptService=ScriptService("192.168.2.2","sbulduk","Sbulduk2024!")

@ScriptBlueprint.route("/executepowershell",methods=["GET"])
def ExecutePowershell():
    scriptContent="Get-Process | Select-Object -First 5"
    try:
        result=scriptService.ExecutePowershell(scriptContent)
        print("Standard Output:",result["stdout"])
        print("Standard Error:",result["stderr"])
        print("Exit Code:",result["status_code"])
        return jsonify({"success":True,"data":f"{result}"}),200
    except Exception as e:
        return({"success":False,"data":f"Check user credentials."})
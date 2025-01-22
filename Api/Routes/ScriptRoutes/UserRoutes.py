from flask import Blueprint,request,jsonify
from API.Services.ScriptServices.UserService import UserService

UserBlueprint=Blueprint("UserBlueprint",__name__,url_prefix="/scripts/user")
userService=UserService("http://192.168.2.2:5985/wsman","sbulduk","Sbulduk2024!")

@UserBlueprint.route("/details/<identity>",methods=["GET"])
def GetUserDetails(identity):
    try:
        result=userService.GetUserDetails(identity)
        return jsonify({"success":True,"data":result}),200
    except Exception as e:
        return jsonify({"success":False,"error":str(e)}),500

@UserBlueprint.route("/add",methods=["POST"])
def AddNewUser():
    try:
        data=request.get_json()
        result=userService.AddNewUser(
            data["name"],
            data["samAccountName"],
            data["displayName"],
            data["initialPassword"],
            data["email"],
            data["ouPath"],
        )
        return jsonify({"success":True,"data":result}),200
    except Exception as e:
        return jsonify({"success":False,"error":str(e)}),500
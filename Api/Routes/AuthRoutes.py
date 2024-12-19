from flask import Blueprint,jsonify,request
from API.Services.AuthService import AuthService
from Models import SessionLocal

AuthBlueprint=Blueprint("AuthBlueprint",__name__,url_prefix="/auth")

def GetAuthService():
    db=SessionLocal()
    try:
        yield AuthService(db)
    finally:
        db.close()

@AuthBlueprint.route("/login",methods=["POST"])
def Login():
    data=request.json
    userName=data.get("userName")
    password=data.get("password")
    
    if not userName or not password:
        return jsonify({"success":False,"data":f"Username and password are required"}),400
    authService=next(GetAuthService())
    token=authService.Login(userName,password)
    return jsonify({"success":True,"data":f"{token}"}),200

@AuthBlueprint.route("/decode",methods=["POST"])
def DecodeToken():
    token=request.headers.get("Authorization","").replace("Bearer","")
    if not token:
        return jsonify({"success":False,"data":f"Token is required"}),400
    authService=next(GetAuthService())
    payload=authService.DecodeJWT(token)
    return jsonify({"success":True,"data":f"{payload}"}),200

@AuthBlueprint.route("/checkuserrole/<string:roleName>")
def CheckUserRole(roleName:str):
    userId=request.args.get("userId")
    if not userId:
        return jsonify({"success":False,"data":f"User ID is required"}),400
    authService=next(GetAuthService())
    hasRole=authService.CheckUserRole(userId,roleName)
    return jsonify({"success":True,"data":f"{hasRole}"}),200
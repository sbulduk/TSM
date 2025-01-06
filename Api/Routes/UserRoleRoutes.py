from flask import Blueprint,jsonify,request
from API.Services.UserService import UserService
from API.Services.RoleService import RoleService
from API.Services.UserRoleService import UserRoleService
from Models import SessionLocal

UserRoleBlueprint=Blueprint("UserRoleBlueprint",__name__,url_prefix="/userrole")
db=SessionLocal()

def GetUserService():
    yield UserService(db)
def GetRoleService():
    yield RoleService(db)
def GetUserRoleService():
    yield UserRoleService(db)

@UserRoleBlueprint.route("/adduserrole",methods=["POST"])
def AddUserRole():
    data=request.json
    userId=data.get("userId")
    roleId=data.get("roleId")

    if not userId or not roleId:
        return jsonify({"success":False,"data":f"User ID and Role ID are compulsory"}),400
    
    userRoleService=next(GetUserRoleService())
    try:
        userRoleService.AddUserRole(userId,roleId)
        return jsonify({"success":True,"data":{
            "message":f"User-Role added successfully",
            "userId":userId,
            "roleId":roleId
        }}),201
    except Exception as e:
        return jsonify({"success":False,"data":f"Error: {e}"})
    
@UserRoleBlueprint.route("/deleteuserrole",methods=["DELETE"])
def DeleteUserRole():
    data=request.json
    userId=data.get("userId")
    roleId=data.get("roleId")

    if not userId or not roleId:
        return jsonify({"success":False,"data":f"User ID and Role ID are compulsory"}),400
    
    userRoleService=next(GetUserRoleService())
    try:
        userRoleService.DeleteUserRole(userId,roleId)
        return jsonify({"success":True,"data":{
            "message":f"User-Role deleted successvully",
            "userId":userId,
            "roleId":roleId
        }})
    except Exception as e:
        return jsonify({"success":False,"data":f"Error: {e}"}),500
    
@UserRoleBlueprint.route("/roles/<string:userId>",methods=["GET"])
def GetRolesofUser(userId:str):
    userService=next(GetUserService())
    user=userService.GetUserbyId(userId)
    if user:
        userRoleService=next(GetUserRoleService())
        try:
            roleList=userRoleService.GetRolesofUser(userId)
            return jsonify({"success":True,"data":{
                "userName":user.UserName,
                "email":user.Email,
                "roleList":roleList
            }})
        except Exception as e:
            return jsonify({"success":False,"data":f"Error: {e}"}),500
    return jsonify({"success":False,"data":f"User ID cannot be found"}),500
        
@UserRoleBlueprint.route("/users/<string:roleId>",methods=["GET"])
def GetUsersofRole(roleId:str):
    roleService=next(GetRoleService())
    role=roleService.GetRolebyId(roleId)
    if role:
        userRoleService=next(GetUserRoleService())
        try:
            userList=userRoleService.GetUsersofRole(roleId)
            return jsonify({"success":False,"data":{
                "roleName":role.Name,
                "userList":userList
            }})
        except Exception as e:
            return jsonify({"success":False,"data":f"Error: {e}"})
    return jsonify({"success":False,"data":f"Role ID cannot be found"}),500
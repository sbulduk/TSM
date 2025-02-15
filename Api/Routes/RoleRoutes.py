from flask import Blueprint,jsonify,request
from API.Services.RoleService import RoleService
from Models import SessionLocal

RoleBlueprint=Blueprint("RoleBlueprint",__name__,url_prefix="/role")

def GetRoleService():
    db=SessionLocal()
    try:
        yield RoleService(db)
    finally:
        db.close()

@RoleBlueprint.route("/getrole/<string:roleId>",methods=["GET"])
def GetRole(roleId:str):
    roleService=next(GetRoleService())
    role=roleService.GetRolebyId(roleId)
    return jsonify({"success":True,"data":{
        "roleName":role.Name,
        "description":role.Description
    }}),201

@RoleBlueprint.route("/listroles",methods=["GET"])
def ListRoles():
    roleService=next(GetRoleService())
    roles=roleService.GetRoleList()
    return jsonify({"success":True,"data":f"{roles}"}),200

@RoleBlueprint.route("/addrole",methods=["POST"])
def AddRole():
    data=request.json
    roleName=data.get("roleName")
    description=data.get("description")

    roleService=next(GetRoleService())
    roleService.AddRole(roleName,description)

    if not roleName:
        return jsonify({"success":False,"data":f"Role name is required"}),400

    roleService=next(GetRoleService())
    roleId=roleService.AddRole(roleName,description)
    return jsonify({"success":True,"data":{
        "message":f"Role added successfully",
        "roleId":roleId
    }}),201

@RoleBlueprint.route("/updaterole/<string:roleId>",methods=["PUT"])
def UpdateRole(roleId:str):
    data=request.json
    roleName=data.get("roleName")
    description=data.get("description")

    roleService=next(GetRoleService())
    role_Id=roleService.GetRolebyId(roleId)

    if role_Id:
        roleService.UpdateRole(roleId,roleName,description)
        return jsonify({"success":True,"data":{
            "message":f"Role updated",
            "roleId":roleId
        }}),200
    return jsonify({"success":False,"data":{
        "message":f"Role Id cannot be found",
        "roleId":roleId
    }}),500
    
@RoleBlueprint.route("/deleterole/<string:roleId>",methods=["DELETE"])
def DeleteRole(roleId:str):
    roleService=next(GetRoleService())
    role_Id=roleService.GetRolebyId(roleId)

    if role_Id:
        result=roleService.DeleteRole(roleId)
        if result:
            return jsonify({"success":True,"data":{
                "message":f"Role deleted",
                "roleId":roleId
            }}),200
        return jsonify({"success":False,"data":f"An error occured"}),400
    return jsonify({"success":False,"data":f"Role cannot be found"}),400
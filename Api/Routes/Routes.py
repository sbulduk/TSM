from flask import Blueprint,jsonify,request

MainBlueprint=Blueprint("MainBlueprint",__name__,url_prefix="/main")

@MainBlueprint.route("/get",methods=["GET"])
def GetData():
    return jsonify({"success":True,"data":f"Get data..."}),200

@MainBlueprint.route("/post",methods=["POST"])
def EchoPost():
    data=request.json
    return jsonify({"success":True,"data":f"{data}"}),201

@MainBlueprint.route("/test",methods=["GET"])
def ShowConfig():
    from Middleware.Config import Config
    # re=Config.settings.to_dict()
    res=Config.settings("JWT")
    print(f"{res}")
    return jsonify({"asdf":res})
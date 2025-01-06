from connexion import FlaskApp

class APIDoc(object):
    @staticmethod
    def RegisterAPIDoc(connexionApp:FlaskApp)->None:
        connexionApp.add_api("Main.yaml",base_path="/main",name="MainAPI")
        connexionApp.add_api("Auth.yaml",base_path="/auth",name="AuthAPI")
        connexionApp.add_api("Role.yaml",base_path="/role",name="RoleAPI")
        connexionApp.add_api("UserRole.yaml",base_path="/userrole",name="UserRoleAPI")
        connexionApp.add_api("Script.yaml",base_path="/script",name="ScriptAPI")
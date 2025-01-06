from connexion import FlaskApp
from API.Routes.Routes import MainBlueprint
from API.Routes.AuthRoutes import AuthBlueprint
from API.Routes.RoleRoutes import RoleBlueprint
from API.Routes.UserRoleRoutes import UserRoleBlueprint
from API.Routes.ScriptRoutes import ScriptBlueprint

class Blueprint(object):
    @staticmethod
    def RegisterBluprint(connexionApp:FlaskApp)->None:
        connexionApp.app.register_blueprint(MainBlueprint,name="MainBlueprint")
        connexionApp.app.register_blueprint(AuthBlueprint,name="AuthBlueprint")
        connexionApp.app.register_blueprint(RoleBlueprint,name="RoleBlueprint")
        connexionApp.app.register_blueprint(UserRoleBlueprint,name="UserRoleBlueprint")
        connexionApp.app.register_blueprint(ScriptBlueprint,name="ScriptBlueprint")
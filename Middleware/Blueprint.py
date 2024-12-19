from connexion import FlaskApp
from API.Routes.Routes import MainBlueprint
from API.Routes.AuthRoutes import AuthBlueprint
from API.Routes.ScriptRoutes import ScriptBlueprint

class Blueprint(object):
    @staticmethod
    def RegisterBluprint(connexionApp:FlaskApp)->None:
        connexionApp.app.register_blueprint(MainBlueprint)
        connexionApp.app.register_blueprint(AuthBlueprint)
        connexionApp.app.register_blueprint(ScriptBlueprint)
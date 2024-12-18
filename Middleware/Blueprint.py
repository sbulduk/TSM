from connexion import FlaskApp
from API.Routes.Routes import MainBlueprint

class Blueprint(object):
    @staticmethod
    def RegisterBluprint(connexionApp:FlaskApp)->None:
        connexionApp.app.register_blueprint(MainBlueprint)
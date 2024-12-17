import connexion
from flask_cors import CORS
from Api.Routes.Routes import MainBlueprint
import uvicorn

class App(object):
    def __init__(self)->None:
        allowedHeaders=["*"]
        self.connexionApp=connexion.FlaskApp(__name__,specification_dir="OpenAPI")
        CORS(self.connexionApp.app, allow_headers=allowedHeaders)
        self.connexionApp.app.register_blueprint(MainBlueprint)
        self.connexionApp.add_api("openapi.yaml")

    def Run(self)->None:
        uvicorn.run(self.connexionApp,host="127.0.0.1",port=8080)

if __name__=="__main__":
    app=App()
    app.Run()
from dotenv import load_dotenv
import connexion
from flask_cors import CORS
from Middleware.Blueprint import Blueprint
from Middleware.APIDoc import APIDoc
import uvicorn

load_dotenv(override=True)

class App(object):
    def __init__(self)->None:
        allowedHeaders=["*"]
        self.connexionApp=connexion.FlaskApp(__name__,specification_dir="OpenAPI")
        CORS(self.connexionApp.app, allow_headers=allowedHeaders)
        Blueprint.RegisterBluprint(self.connexionApp)
        APIDoc.RegisterAPIDoc(self.connexionApp)
        # self.connexionApp.add_api("Main.yaml")

    def Run(self)->None:
        uvicorn.run(self.connexionApp,host="127.0.0.1",port=8888)

if __name__=="__main__":
    app=App()
    app.Run()
from connexion import FlaskApp

class APIDoc(object):
    @staticmethod
    def RegisterAPIDoc(connexionApp:FlaskApp)->None:
        # specPath=os.path.join(connexionApp.options.get("specification_dir",""),"Master.yaml")
        # print(f"Loading OpenAPI spec from {specPath}")
        # connexionApp.add_api("Master.yaml",base_path="/api",validate_responses=True)

        connexionApp.add_api("Main.yaml",base_path="/main",name="MainAPI")
        connexionApp.add_api("Auth.yaml",base_path="/auth",name="AuthAPI")
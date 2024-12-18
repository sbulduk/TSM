from dynaconf import Dynaconf

class Config(object):
    settings=Dynaconf(
        envvarPrefix="TSM",
        settingsFiles=[
            "Config/DBSettings.toml",
            "Config/GenericSettings.toml"
        ],
        dotenvPath=".env"
    )
from dynaconf import Dynaconf

class Config(object):
    settings=Dynaconf(
        envvarPrefix="TSM",
        settings_files=[
            "./Config/DBSettings.toml",
            "./Config/GenericSettings.toml"
        ],
        dotenvPath=".env"
    )
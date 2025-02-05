import os
from dynaconf import Dynaconf

class Config(object):
    currentPath=os.path.dirname(os.path.abspath(__file__))

    dbSettingsPath=os.path.join(currentPath,"Config","DBSettings.toml")
    genericSettingsPath=os.path.join(currentPath,"Config","GenericSettings.toml")
    remoteAuthPath=os.path.join(currentPath,"Config","RemoteAuth.toml")

    settings=Dynaconf(
        envvarPrefix="TSM",
        settings_files=[
            dbSettingsPath,
            genericSettingsPath,
            remoteAuthPath
        ],
        dotenvPath=".env"
    )
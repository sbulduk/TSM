from structlog import get_logger

class LogService(object):
    def __init__(self)->None:
        self.logger=get_logger()

    def Log(self,level:str,message:str,**kwargs:object)->None:
        getattr(self.logger,level)(message,**kwargs)
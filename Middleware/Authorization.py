from Models import SessionLocal
from functools import wraps
from flask import request
from API.Services.AuthService import AuthService

class Authorization(object):
    def __init__(self):
        self.db=SessionLocal
    
    def __del__(self):
        self.db.close_all()

    def Authorize(self,requiredRoles:list[str])->any:
        def Decorator(f):
            @wraps(f)
            def Wrapper(*args,**kwargs):
                token=request.headers.get("Authorization","").replace("Bearer","")
                if not token:
                    return "Token is required"
                
                try:
                    authService=AuthService(self.db)
                    if not authService.Authorize(token,requiredRoles):
                        return "Access forbidden"
                except ValueError as e:
                    return str(e)
                
                return f(*args,**kwargs)
            return Wrapper
        return Decorator
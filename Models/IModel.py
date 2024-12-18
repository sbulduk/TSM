from . import Base
from sqlalchemy import Column,Boolean

class IModel(Base):
    __abstract__=True
    IsActive=Column(Boolean,nullable=False,default=True)
from ..database import Base
from elrahapi.middleware import models

class Log(Base, models.LogModel):
    __tablename__ = "loggers"
metadata = Base.metadata

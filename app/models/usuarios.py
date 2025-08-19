from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nombre = Column(String)
    edad = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


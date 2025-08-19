from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    email: str
    edad: Optional[int] = None

class UsuarioCrear(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True  
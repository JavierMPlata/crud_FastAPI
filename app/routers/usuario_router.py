from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.models.db import get_db
from app.schemas.usuario_esquemas import UsuarioCrear, UsuarioResponse
from app.services.usuario_service import UsuarioService

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]   
)

@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario: UsuarioCrear, db: Session = Depends(get_db)):
    """Crear un nuevo usuario"""
    return UsuarioService.crear_usuario(db, usuario)

@router.get("/", response_model=List[UsuarioResponse])
def obtener_usuarios(
    skip: int = Query(0, ge=0), 
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Obtener lista de usuarios con paginación"""
    return UsuarioService.obtener_usuarios(db, skip, limit)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Obtener usuario por ID"""
    return UsuarioService.obtener_usuario_por_id(db, usuario_id)

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, usuario: UsuarioCrear, db: Session = Depends(get_db)):
    """Actualizar usuario existente"""
    return UsuarioService.actualizar_usuario(db, usuario_id, usuario)

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Eliminar usuario por ID"""
    UsuarioService.eliminar_usuario(db, usuario_id)
    return {"message": "Usuario eliminado correctamente"}


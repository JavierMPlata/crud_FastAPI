from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.usuarios import Usuario
from app.schemas.usuario_esquemas import UsuarioCrear, UsuarioResponse
from typing import List, Optional

class UsuarioService:
    
    @staticmethod
    def crear_usuario(db: Session, usuario: UsuarioCrear) -> Usuario:
        """Crear un nuevo usuario"""
        # Verificar si el email ya existe
        db_usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
        if db_usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        
        db_usuario = Usuario(
            nombre=usuario.nombre,
            email=usuario.email,
            edad=usuario.edad
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    
    @staticmethod
    def obtener_usuarios(db: Session, skip: int = 0, limit: int = 100) -> List[Usuario]:
        """Obtener lista de usuarios con paginación"""
        return db.query(Usuario).offset(skip).limit(limit).all()
    
    @staticmethod
    def obtener_usuario_por_id(db: Session, usuario_id: int) -> Usuario:
        """Obtener usuario por ID"""
        db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not db_usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        return db_usuario
    
    @staticmethod
    def actualizar_usuario(db: Session, usuario_id: int, usuario: UsuarioCrear) -> Usuario:
        """Actualizar usuario existente"""
        db_usuario = UsuarioService.obtener_usuario_por_id(db, usuario_id)
        
        # Verificar si el nuevo email ya existe (si es diferente al actual)
        if usuario.email != db_usuario.email:
            usuario_con_email = db.query(Usuario).filter(Usuario.email == usuario.email).first()
            if usuario_con_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El email ya está en uso"
                )
        
        # Actualizar campos
        db_usuario.nombre = usuario.nombre
        db_usuario.email = usuario.email
        db_usuario.edad = usuario.edad
        
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    
    @staticmethod
    def eliminar_usuario(db: Session, usuario_id: int) -> bool:
        """Eliminar usuario por ID"""
        db_usuario = UsuarioService.obtener_usuario_por_id(db, usuario_id)
        db.delete(db_usuario)
        db.commit()
        return True
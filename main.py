from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.models.db import Base, engine, test_connection
from app.routers.usuario_router import router as usuario_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Iniciando aplicación...")
    
    # Verificar conexión a la base de datos
    if test_connection():
        print("✅ Base de datos conectada correctamente")
    else:
        print("❌ Error al conectar con la base de datos")
    
    # Crear tablas si no existen
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tablas verificadas/creadas correctamente")
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")
    
    yield
    
    # Shutdown
    print("⏹️ Cerrando aplicación...")

app = FastAPI(
    title="Mi API de Usuarios",
    description="Una API simple para gestionar usuarios con Supabase",
    version="1.0.0",
    lifespan=lifespan
)

# Incluir routers
app.include_router(usuario_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    """Endpoint para verificar el estado de la aplicación y base de datos"""
    db_status = test_connection()
    return {
        "status": "healthy" if db_status else "unhealthy",
        "database": "connected" if db_status else "disconnected"
    }
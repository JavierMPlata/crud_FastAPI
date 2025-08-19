import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables
load_dotenv()

# Fetch variables (funciona tanto para .env local como para GitHub Actions)
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("db_port")  # Cambiar nombre para evitar conflictos
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
if all([USER, PASSWORD, HOST, PORT, DBNAME]):
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
    print(f"🔗 Conectando a Supabase: {HOST}:{PORT}")
else:
    # Para pruebas locales cuando no hay configuración completa
    DATABASE_URL = "sqlite:///./test_local.db"
    print("⚠️  Usando SQLite local para desarrollo/testing")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# Si usas Transaction Pooler o Session Pooler, descomenta la siguiente línea:
# engine = create_engine(DATABASE_URL, poolclass=NullPool)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Test the connection (mejorado)
def test_connection():
    try:
        with engine.connect() as connection:
            # Ejecutar una consulta simple para verificar la conexión
            result = connection.execute(text("SELECT 1"))
            result.fetchone()
            return True
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        return False
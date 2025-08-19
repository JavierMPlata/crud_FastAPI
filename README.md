# 🚀 API CRUD de Usuarios

Una API REST moderna y robusta para la gestión de usuarios construida con **FastAPI** y **PostgreSQL/Supabase**.

## 📋 Características

- ✅ **CRUD completo** - Crear, Leer, Actualizar y Eliminar usuarios
- ⚡ **FastAPI** - Framework web de alto rendimiento
- 🐘 **PostgreSQL** - Base de datos robusta con soporte para Supabase
- 📊 **SQLAlchemy ORM** - Manejo elegante de la base de datos
- 🔍 **Validación de datos** - Usando Pydantic schemas
- 📖 **Documentación automática** - Swagger UI integrado
- 🔒 **Validaciones** - Email único y manejo de errores
- ⚡ **Paginación** - Para consultas optimizadas
- 🏥 **Health Check** - Monitor de estado de la aplicación

## 🏗️ Arquitectura del Proyecto

```
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
└── app/
    ├── models/
    │   ├── db.py          # Configuración de base de datos
    │   └── usuarios.py    # Modelo de Usuario (SQLAlchemy)
    ├── routers/
    │   └── usuario_router.py    # Endpoints de la API
    ├── schemas/
    │   └── usuario_esquemas.py  # Validaciones Pydantic
    └── services/
        └── usuario_service.py   # Lógica de negocio
```

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8+
- PostgreSQL (o cuenta de Supabase)
- Git

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd CRUD
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
# Configuración de Base de Datos (Supabase/PostgreSQL)
user=tu_usuario
password=tu_contraseña
host=tu_host
db_port=5432
dbname=tu_base_de_datos
```

### 5. Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

## 📚 Documentación de la API

### Documentación Interactiva

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Mensaje de bienvenida |
| `GET` | `/health` | Estado de la aplicación |
| `POST` | `/usuarios/` | Crear nuevo usuario |
| `GET` | `/usuarios/` | Listar usuarios (con paginación) |
| `GET` | `/usuarios/{id}` | Obtener usuario por ID |
| `PUT` | `/usuarios/{id}` | Actualizar usuario |
| `DELETE` | `/usuarios/{id}` | Eliminar usuario |

### Ejemplos de Uso

#### Crear Usuario
```bash
curl -X POST "http://localhost:8000/usuarios/" \
     -H "Content-Type: application/json" \
     -d '{
       "nombre": "Juan Pérez",
       "email": "juan@ejemplo.com",
       "edad": 30
     }'
```

#### Listar Usuarios (con paginación)
```bash
curl "http://localhost:8000/usuarios/?skip=0&limit=10"
```

#### Obtener Usuario por ID
```bash
curl "http://localhost:8000/usuarios/1"
```

#### Actualizar Usuario
```bash
curl -X PUT "http://localhost:8000/usuarios/1" \
     -H "Content-Type: application/json" \
     -d '{
       "nombre": "Juan Carlos",
       "email": "juan.carlos@ejemplo.com",
       "edad": 31
     }'
```

#### Eliminar Usuario
```bash
curl -X DELETE "http://localhost:8000/usuarios/1"
```

## 📊 Modelo de Datos

### Usuario

```python
{
  "id": int,              # ID único (auto-generado)
  "nombre": str,          # Nombre del usuario
  "email": str,           # Email único
  "edad": int | null,     # Edad (opcional)
  "created_at": datetime  # Fecha de creación
}
```

## 🛠️ Tecnologías Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno y rápido
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para Python
- **[Pydantic](https://pydantic.dev/)** - Validación de datos
- **[PostgreSQL](https://www.postgresql.org/)** - Base de datos relacional
- **[Supabase](https://supabase.com/)** - Backend como servicio
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **[psycopg2](https://pypi.org/project/psycopg2/)** - Adaptador de PostgreSQL

## 🔧 Desarrollo

### Estructura de Carpetas

- **`models/`**: Modelos de SQLAlchemy y configuración de DB
- **`routers/`**: Definición de endpoints de la API
- **`schemas/`**: Esquemas de Pydantic para validación
- **`services/`**: Lógica de negocio y operaciones CRUD

### Flujo de Datos

1. **Router** recibe la petición HTTP
2. **Schema** valida los datos de entrada
3. **Service** ejecuta la lógica de negocio
4. **Model** interactúa con la base de datos
5. **Response** devuelve los datos validados

## 🔍 Health Check

Verificar el estado de la aplicación:

```bash
curl http://localhost:8000/health
```

Respuesta esperada:
```json
{
  "status": "healthy",
  "database": "connected"
}
```

## 🐛 Manejo de Errores

La API maneja los siguientes errores:

- **400 Bad Request**: Email duplicado
- **404 Not Found**: Usuario no encontrado
- **422 Unprocessable Entity**: Datos de entrada inválidos
- **500 Internal Server Error**: Error del servidor

## 📝 Logs

La aplicación incluye logs informativos:
- ✅ Conexión exitosa a la base de datos
- ✅ Tablas creadas/verificadas
- ❌ Errores de conexión o configuración

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abrir un Pull Request


⭐ ¡No olvides dar una estrella si este proyecto te fue útil!

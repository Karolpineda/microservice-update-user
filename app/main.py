# app/main.py
from fastapi import FastAPI
from app.controllers import user  # Rutas de la aplicación
from app.database import engine
from app.models import Base
from app.docs import swagger_router  # Importar swagger_router

app = FastAPI(
    title="Mi API",
    description="Documentación personalizada de mi API",
    version="1.0.0",
    docs_url=None,    # Deshabilita /docs por defecto
    redoc_url=None    # Deshabilita /redoc
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas de la aplicación
app.include_router(user.router)
app.include_router(swagger_router)  # Incluir el router de Swagger
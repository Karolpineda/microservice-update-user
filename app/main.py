# app/main.py
from fastapi import FastAPI
from app.controllers import user  # Importa el controlador de usuario
from app.database import engine
from app.models import Base

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas de usuario
app.include_router(user.router)

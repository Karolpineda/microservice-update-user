

from fastapi import FastAPI
from app.controllers import user  # Solo importa el controlador de actualización
from app.docs import swagger_router  # Importar swagger_router

app = FastAPI(
    title="API de actualización de usuarios",
    description="Microservicio para la actualización de usuarios",
    version="1.0.0",
)

# Incluir las rutas de actualización de usuarios
app.include_router(user.router)

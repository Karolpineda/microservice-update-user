from pydantic import BaseModel
from uuid import UUID
from typing import Optional

# app/schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    class Config:
        orm_mode = True


# Esquema para la actualización de un usuario
class UserUpdate(UserBase):
    password: Optional[str] = None  # Si deseas permitir la actualización de la contraseña

# Esquema para los datos del usuario que se devolverán
class UserOut(UserBase):
    id: UUID

    class Config:
        orm_mode = True  # Esto permite que Pydantic trabaje con los objetos de SQLAlchemy

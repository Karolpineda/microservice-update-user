from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserUpdate(UserBase):
    password: Optional[str] = None  # Si deseas permitir la actualización de la contraseña

class UserOut(UserBase):
    id: UUID

    class Config:
        orm_mode = True  # Esto permite que Pydantic trabaje con los objetos de SQLAlchemy

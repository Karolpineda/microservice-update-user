from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
import uuid

# Creamos el contexto para encriptar y verificar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para hashear la contraseña
def hash_password(password: str):
    return pwd_context.hash(password)

# Función para verificar la contraseña
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Función para actualizar un usuario
def update_user(db: Session, user_id: str, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.email = user.email

    if user.password:  # Si se quiere actualizar la contraseña
        db_user.password = hash_password(user.password)
    
    db.commit()
    db.refresh(db_user)
    return db_user

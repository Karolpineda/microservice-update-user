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

# Crear un nuevo usuario
def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)  # Hashear la contraseña
    db_user = User(id=str(uuid.uuid4()),  # Generar UUID
                   first_name=user.first_name, last_name=user.last_name, 
                   email=user.email, password=hashed_password)  # Guardar la contraseña hasheada
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener un usuario por correo electrónico
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Obtener un usuario por ID
def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()
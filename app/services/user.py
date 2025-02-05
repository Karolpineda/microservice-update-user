# app/services/user.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserUpdate


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

# Función para actualizar un usuario
def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        return None
    
    # Actualizar los campos del usuario
    db_user.first_name = user.first_name or db_user.first_name
    db_user.last_name = user.last_name or db_user.last_name
    db_user.email = user.email or db_user.email
    db_user.password = user.password or db_user.password
    
    db.commit()
    db.refresh(db_user)
    
    return db_user

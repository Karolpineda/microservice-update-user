from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database  # Importaciones generales
from app.services.user import update_user  # Importación desde services/user.py

router = APIRouter()

# Ruta Health para verificar si el microservicio está activo
@router.get("/health")
def health_check():
    return {"status": "Microservice Users (Update) is up and running"}

# Ruta para actualizar un usuario
@router.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user_route(user_id: str, user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user and db_user.id != user_id:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return update_user(db=db, user_id=user_id, user=user)

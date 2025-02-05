from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database  # Importaciones generales
from app.schemas.user import UserBase, UserCreate, UserOut
from app.services.user import get_user_by_email, create_user, verify_password  # Importaciones desde services/user.py

router = APIRouter()

# Ruta Health para verificar si el microservicio está activo
@router.get("/health")
def health_check():
    return {"status": "Microservice Users is up and running"}

@router.post("/users/", response_model=schemas.UserOut)  # Aquí se utiliza UserOut
def create_user_route(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Verificar si la contraseña coincide
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful"}
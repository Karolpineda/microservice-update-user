# app/controllers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database
from app.services.user import update_user, get_user_by_id


router = APIRouter()

# Ruta para actualizar un usuario
@router.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user_route(user_id: str, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    # Verificar si el usuario existe
    db_user = get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Actualizar los campos
    return update_user(db=db, user_id=user_id, user=user)


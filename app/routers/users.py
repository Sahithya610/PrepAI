from fastapi import APIRouter
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.user import create_user, update_user
from fastapi import HTTPException, status
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
def me(current_user: User= Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserResponse)
def up_user(user_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_user(db, user_data, current_user)




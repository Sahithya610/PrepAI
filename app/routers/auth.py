from fastapi import APIRouter
from app.schemas.user import UserCreate, UserLogin
from app.services.user import login_user
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.auth import Token
from fastapi import Depends
router = APIRouter(prefix="/auth", tags=["users"])

users = []

@router.post("/register", status_code=201, response_model=UserCreate)
def register(user: UserCreate):
    new_user = {
        "name" : user.name,
        "email": user.email,
        "password":user.password
    }
    users.append(new_user)
    return {"message": "authentication okay"}

@router.post("/login", status_code=200, response_model=Token)
def login(login : UserLogin, db: Session=Depends(get_db)):
    token =login_user(db, login.email, login.password)
    return Token(access_token=token, token_type="bearer")


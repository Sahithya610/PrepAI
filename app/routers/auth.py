from fastapi import APIRouter
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.user import login_user, create_user
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.auth import Token
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["users"])


@router.post("/register", status_code=201, response_model=UserResponse)
def register(user: UserCreate, db: Session=Depends(get_db)):
    return create_user(db, user)

@router.post("/login", status_code=200, response_model=Token)
def login(form_data : OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    token =login_user(db, form_data.username, form_data.password)
    return Token(access_token=token, token_type="bearer")


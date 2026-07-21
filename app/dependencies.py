from fastapi import Depends
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.config import settings
from app.models.user import User
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = '/auth/login')

def get_current_user(token: str=Depends(oauth2_scheme), db:Session=Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email = payload["sub"]
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user
    else: 
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail = "User not Found"
        )

from fastapi import APIRouter
from app.schemas.user import UserResponse, UserCreate
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.user import create_user
from fastapi import HTTPException, status


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def me(page:int=1, limit:int=10):
    return{"message":"got me"}

@router.put("/me")
def put_me():
    return{"message":"put me"}

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def post_me(user : UserCreate,db: Session=Depends(get_db)):
    return create_user(db,user)

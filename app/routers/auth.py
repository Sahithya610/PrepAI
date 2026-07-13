from fastapi import APIRouter
from app.schemas.user import UserCreate, UserLogin
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

@router.post("/login", status_code=201)
def login(login : UserLogin):
    return {"message": "login successful"}


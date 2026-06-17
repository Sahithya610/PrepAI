from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["users"])

@router.post("/register", status_code=201)
def register():
    return {"message": "authentication okay"}

@router.post("/login", status_code=201)
def login():
    return {"message": "login successful"}


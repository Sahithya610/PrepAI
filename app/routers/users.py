from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def me(page:int=1, limit:int=10):
    return{"message":"got me"}

@router.put("/me")
def put_me():
    return{"message":"put me"}
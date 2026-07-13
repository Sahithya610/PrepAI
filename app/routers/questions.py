from fastapi import APIRouter

router = APIRouter(prefix="/questions", tags=["questions"])

@router.post("/{id}/feedback", status_code=201)
def feedback():
    return{"message":"Get AI feedback"}

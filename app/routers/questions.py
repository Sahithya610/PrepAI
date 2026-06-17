from fastapi import APIRouter

router = APIRouter(prefix="/questions", tags=["questions"])

@router.post("/{id}/feedback")
def feedback():
    return{"message":"Get AI feedback"}

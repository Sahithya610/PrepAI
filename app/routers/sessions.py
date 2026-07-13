from fastapi import APIRouter, status, HTTPException
from app.schemas.session import SessionCreate, SessionUpdate, SessionResponse

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SessionResponse)
def create_sessions(session : SessionCreate):
    return{"message":"created session"}

@router.get("/", status_code=status.HTTP_200_OK)
def get_sessions(page: int=1, limit: int=10):
    return {"message":"displayed all sessions"}

@router.get("/{session_id}",status_code=status.HTTP_200_OK)
def get_one_sess(session_id: int):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Session {session_id} not found"
    )

@router.delete("/{id}")
def delete_sess(id : int):
    return{"message":"deleted session"}

@router.post("/{id}/questions", status_code=status.HTTP_201_CREATED)
def add_questions():
    return{"message":"added questions"}

@router.get("/{id}/questions")
def get_questions():
    return{"message":"List questions"}
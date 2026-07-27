from fastapi import APIRouter, Depends
from app.schemas.question import QuestionCreate, QuestionResponse
from app.services.question import add_question
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.dependencies import get_current_user

router = APIRouter(prefix="/sessions", tags=["questions"])

@router.post("/{session_id}/questions", response_model=QuestionResponse, status_code=201)
def create_quest(session_id:str, question_data:QuestionCreate, db: Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    return add_question(db, session_id, question_data, current_user)

@router.post("/{id}/feedback", status_code=201)
def feedback():
    return{"message":"Get AI feedback"}
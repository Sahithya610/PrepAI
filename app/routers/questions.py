from fastapi import APIRouter, Depends
from app.schemas.question import QuestionCreate, QuestionResponse, SubmitAnswer
from app.services.question import add_question, submit_answer, get_feedback
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.dependencies import get_current_user

router = APIRouter(prefix="/sessions", tags=["questions"])

@router.post("/{session_id}/questions", response_model=QuestionResponse, status_code=201)
def create_quest(session_id:str, question_data:QuestionCreate, db: Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    return add_question(db, session_id, question_data, current_user)

@router.post("/{question_id}/feedback", response_model=QuestionResponse)
async def feedback(question_id:str, db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return await get_feedback(db, question_id, current_user)

@router.patch("/{question_id}/answer", response_model=QuestionResponse)
def send_answer(question_id: str, answer: SubmitAnswer, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return submit_answer(db, question_id, answer.user_answer, current_user)
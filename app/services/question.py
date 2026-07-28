from app.services.session import get_session
from app.models.question import Question
from fastapi import HTTPException, status
from app.models.session import InterviewSession
from app.services.ai_service import get_ai_feedback
import json
def add_question(db, session_id, question_data, current_user):
    session = get_session(db, session_id, current_user)
    new_question = Question(
        session_id = session_id,
        question_text = question_data.question_text
    )
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

def submit_answer(db, question_id, answer, current_user):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    session = db.query(InterviewSession).filter(InterviewSession.id == question.session_id).first()
    if session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Invalid user")
    question.user_answer = answer
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

async def get_feedback(db, question_id, current_user):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )
    session = db.query(InterviewSession).filter(InterviewSession.id == question.session_id).first()
    if session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Invalid user")
    if not question.user_answer:
        raise HTTPException(
            status_code=404,
            detail="User hasn't given an answer"
        )
    ai_result = await get_ai_feedback(question.question_text, question.user_answer)
    feedback = json.loads(ai_result)
    question.ai_feedback = feedback["feedback"]
    question.score = feedback["score"]
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

from app.services.session import get_session
from app.models.question import Question
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
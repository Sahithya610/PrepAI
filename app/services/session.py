from app.models.session import InterviewSession
from fastapi import HTTPException, status

def create_session(db, session_data, current_user):
    new_session = InterviewSession(
        user_id = current_user.id,
        title = session_data.title,
        role = session_data .role,
        difficulty = session_data.difficulty
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

def get_sessions(db, current_user, skip:int=0, limit:int=10):
    sessions = db.query(InterviewSession).filter(InterviewSession.user_id == current_user.id).offset(skip).limit(limit).all()
    return sessions

def get_session(db, session_id, current_user):
    session = db.query(InterviewSession).filter(InterviewSession.id == session_id, InterviewSession.user_id==current_user.id).first()
    if session:
        return session
    else: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail ="Session not found"
        )
    
def update_session(db, session_id, session_data, current_user):
    session = get_session(db, session_id, current_user)
    for field, value in session_data.model_dump(exclude_unset=True).items():
        setattr(session, field, value)
    db.commit()
    db.refresh(session)
    return session

def delete_session(db, session_id, current_user):
    session = get_session(db, session_id, current_user)
    db.delete(session)
    db.commit()
    return
from fastapi import APIRouter, status, HTTPException
from app.schemas.session import SessionCreate, SessionUpdate, SessionResponse
from app.services.session import create_session
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.session import InterviewSession
from app.dependencies import get_current_user
from app.services.session import get_sessions, get_session, update_session, delete_session
from typing import List


router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SessionResponse)
def session(session_data: SessionCreate, db: Session = Depends(get_db), current_user : User=Depends(get_current_user)):
    return create_session(db, session_data, current_user)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[SessionResponse])
def list_sessions(page: int=1, limit: int=10, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    skip = (page-1)*limit
    return get_sessions(db, current_user, skip, limit)

@router.get("/{session_id}",status_code=status.HTTP_200_OK, response_model=SessionResponse)
def get_sess(session_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_session(db, session_id, current_user)

@router.put("/{session_id}", response_model=SessionResponse)
def update(session_id: str, session_data: SessionUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_session(db, session_id, session_data, current_user)

@router.delete("/{session_id}", status_code=204)
def delete_sess(session_id:str, db:Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    return delete_session(db, session_id, current_user)

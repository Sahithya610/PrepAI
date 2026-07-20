from app.utils.security import hash_password
from app.models.user import User
from fastapi import HTTPException, status
def create_user(db, user_data):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    else: 
        new_user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=hash_password(user_data.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
from app.utils.security import hash_password
from app.models.user import User
from fastapi import HTTPException, status
from app.utils.security import create_access_token, decode_access_token, verify_password

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
    
def login_user(db, email, password):
    user = db.query(User).filter(User.email == email).first()
    if user:
       if verify_password(password, user.hashed_password):
           return create_access_token({"sub":user.email})
       else: 
           raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail = "Incorrect password"
           )
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "User not found"
        )

def update_user(db, user_data, current_user):
    for field, value in user_data.model_dump(exclude_unset=True).items():
        setattr(current_user, field, value)
    db.commit()
    db.refresh(current_user)
    return current_user
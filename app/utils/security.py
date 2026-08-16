import bcrypt
from jose import jwt, JWTError
from app.config import settings
from datetime import datetime, timedelta, timezone

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    result = bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    return result

def create_access_token(data: dict) -> str:
    new_data = data.copy()
    new_data["exp"] = datetime.now(timezone.utc) + timedelta(minutes=30)
    return jwt.encode(new_data, settings.SECRET_KEY, algorithm='HS256')
    
def decode_access_token(token:str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        return None
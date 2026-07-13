from fastapi import FastAPI
from dotenv import load_dotenv
from datetime import datetime
from app.database import Base, engine
from app.routers import sessions, users, auth, questions
import os

load_dotenv()

app = FastAPI()

@app.get("/health")
def health():
    return{
        "status": "ok",
        "app": "PrepAI",
        "version":os.getenv("APP_VERSION"),
        "timestamp": datetime.now().isoformat()
    }
app.include_router(sessions.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(questions.router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


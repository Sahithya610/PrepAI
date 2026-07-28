from fastapi import FastAPI
from datetime import datetime
from app.database import Base, engine
from app.routers import sessions, users, auth, questions
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return{
        "status": "ok",
        "app": "PrepAI",
        "version":settings.APP_VERSION,
        "timestamp": datetime.now().isoformat()
    }
app.include_router(sessions.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(questions.router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


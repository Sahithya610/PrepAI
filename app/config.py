from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "PrepAI"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    GROQ_API_KEY: str
    FRONTEND_URL: str = "http://localhost:3000"

    model_config = {
        "extra": "ignore",
        "env_file": ".env",
    }


settings = Settings()


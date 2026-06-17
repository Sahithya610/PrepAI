from fastapi import FastAPI
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
import os
import importlib

load_dotenv()

app = FastAPI()

@app.get("/health")
def health():
    return{
        "status": "ok",
        "app": "PrepAI",
        "version":os.getenv("APP_NAME"),
        "timestamp": datetime.now().isoformat()
    }

routers_dir = Path(__file__).parent/"routers"

for file in routers_dir.glob("*.py"):
    if file.stem.startswith("_"):
        continue

    module = importlib.import_module(f"routers.{file.stem}")

    if hasattr(module, "router"):
        app.include_router(module.router)



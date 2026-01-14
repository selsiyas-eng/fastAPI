from fastapi import FastAPI
from backend.core.config import settings

app = FastAPI()


@app.get("/")
def hello():
    return {"msg": "Hello FastAPI"}

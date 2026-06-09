from fastapi import FastAPI
from routes import router

app = FastAPI(title="API Turismo")

app.include_router(router)


@app.get("/")
def home():
    return {"mensaje": "API funcionando"}
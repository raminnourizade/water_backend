
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import readings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="WaterM Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(readings.router)

@app.get("/")
def home():
    return {"message": "Backend is running. Use /docs to test the API."}

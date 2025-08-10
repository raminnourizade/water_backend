from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, database

app = FastAPI()

# ایجاد جداول در صورت نبودن
models.Base.metadata.create_all(bind=database.engine)

# Dependency برای گرفتن session از دیتابیس
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ API ثبت رکورد جدید
@app.post("/readings/", response_model=schemas.ReadingOut)
def create_reading(reading: schemas.ReadingCreate, db: Session = Depends(get_db)):
    db_reading = models.Reading(**reading.dict())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading

# ✅ API دریافت همه رکوردها (مرتب‌سازی بر اساس زمان ثبت)
@app.get("/readings/", response_model=list[schemas.ReadingOut])
def get_all_readings(db: Session = Depends(get_db)):
    return db.query(models.Reading).order_by(models.Reading.created_at.desc()).all()

# 🔄 صفحه خانه ساده برای تست
@app.get("/")
def home():
    return {"message": "Backend is running. Use /docs to test the API."}

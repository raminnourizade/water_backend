
from sqlalchemy.orm import Session
from . import models, schemas

def create_reading(db: Session, data: schemas.ReadingCreate) -> models.Reading:
    obj = models.Reading(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def list_readings(db: Session):
    return db.query(models.Reading).order_by(models.Reading.created_at.desc()).all()

def get_reading(db: Session, reading_id: int):
    return db.query(models.Reading).filter(models.Reading.id == reading_id).first()

def update_reading(db: Session, reading_id: int, data: schemas.ReadingUpdate):
    obj = get_reading(db, reading_id)
    if not obj:
        return None
    for k, v in data.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_reading(db: Session, reading_id: int) -> bool:
    obj = get_reading(db, reading_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True

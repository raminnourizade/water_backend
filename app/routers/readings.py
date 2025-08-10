
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, crud
from ..deps import get_db

router = APIRouter(prefix="/readings", tags=["readings"])

@router.post("/", response_model=schemas.ReadingOut)
def create_reading(reading: schemas.ReadingCreate, db: Session = Depends(get_db)):
    return crud.create_reading(db, reading)

@router.get("/", response_model=List[schemas.ReadingOut])
def get_all_readings(
    db: Session = Depends(get_db),
    user_id: Optional[str] = None,
    start: Optional[str] = Query(None, description="ISO date"),
    end: Optional[str] = Query(None, description="ISO date"),
):
    items = crud.list_readings(db)
    if user_id:
        items = [i for i in items if i.user_id == user_id]
    from datetime import datetime
    def parse_dt(s): 
        try: 
            return datetime.fromisoformat(s) if s else None
        except Exception: 
            return None
    start_dt = parse_dt(start); end_dt = parse_dt(end)
    if start_dt:
        items = [i for i in items if i.created_at >= start_dt]
    if end_dt:
        items = [i for i in items if i.created_at <= end_dt]
    return items

@router.get("/{reading_id}", response_model=schemas.ReadingOut)
def get_reading(reading_id: int, db: Session = Depends(get_db)):
    obj = crud.get_reading(db, reading_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Reading not found")
    return obj

@router.put("/{reading_id}", response_model=schemas.ReadingOut)
def update_reading(reading_id: int, data: schemas.ReadingUpdate, db: Session = Depends(get_db)):
    obj = crud.update_reading(db, reading_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Reading not found")
    return obj

@router.delete("/{reading_id}", status_code=204)
def delete_reading(reading_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_reading(db, reading_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Reading not found")
    return None

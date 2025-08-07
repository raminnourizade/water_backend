
from pydantic import BaseModel
from datetime import datetime

class ReadingCreate(BaseModel):
    user_id: str
    lat: float
    lon: float
    value: float

class ReadingOut(ReadingCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

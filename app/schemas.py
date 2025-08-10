
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReadingBase(BaseModel):
    user_id: Optional[str] = None
    main_subscription: str
    sub_subscription: Optional[str] = None
    address: str
    lat: float
    lng: float
    altitude: Optional[float] = None
    accuracy: Optional[float] = None
    image_path: Optional[str] = None

class ReadingCreate(ReadingBase):
    created_at: Optional[datetime] = None

class ReadingUpdate(BaseModel):
    user_id: Optional[str] = None
    main_subscription: Optional[str] = None
    sub_subscription: Optional[str] = None
    address: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    altitude: Optional[float] = None
    accuracy: Optional[float] = None
    image_path: Optional[str] = None
    created_at: Optional[datetime] = None

class ReadingOut(ReadingBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

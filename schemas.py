from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReadingBase(BaseModel):
    user_id: Optional[str]
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

class ReadingOut(ReadingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

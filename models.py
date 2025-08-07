
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    lat = Column(Float)
    lon = Column(Float)
    value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

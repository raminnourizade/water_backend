
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)

    main_subscription = Column(String, nullable=False)
    sub_subscription = Column(String, nullable=True)
    address = Column(String, nullable=False)

    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    altitude = Column(Float, nullable=True)
    accuracy = Column(Float, nullable=True)

    image_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

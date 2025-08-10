from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)  # کلید اصلی
    user_id = Column(String, index=True)  # شناسه کاربر ثبت کننده

    main_subscription = Column(String, nullable=False)       # اشتراک اصلی
    sub_subscription = Column(String, nullable=True)         # اشتراک فرعی (اختیاری)
    address = Column(String, nullable=False)                 # آدرس

    lat = Column(Float, nullable=False)                      # عرض جغرافیایی
    lng = Column(Float, nullable=False)                      # طول جغرافیایی
    altitude = Column(Float, nullable=True)                  # ارتفاع
    accuracy = Column(Float, nullable=True)                  # دقت GPS

    image_path = Column(String, nullable=True)               # مسیر عکس (در سرور یا کلاینت)
    created_at = Column(DateTime, default=datetime.utcnow)   # زمان ثبت

    def __repr__(self):
        return f"<Reading(main_subscription={self.main_subscription}, lat={self.lat}, lng={self.lng})>"

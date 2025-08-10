
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "WaterM Backend"
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    DATABASE_URL: str = "sqlite:///./app.db"
    JWT_SECRET: str = "change_me"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    class Config:
        env_file = ".env"

settings = Settings()

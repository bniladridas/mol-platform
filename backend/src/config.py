from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API security
    API_KEY: str = "your-secret-api-key"  # Change in production

    # Celery settings (for future async processing)
    CELERY_BROKER_URL: str = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

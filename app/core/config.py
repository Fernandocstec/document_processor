from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional
import os
from pathlib import Path

class Settings(BaseSettings):
    # Application Settings
    APP_NAME: str
    APP_ENV: str
    DEBUG: bool

    # Model Settings
    YOLO_MODEL_PATH: str
    CONFIDENCE_THRESHOLD: float
    IOU_THRESHOLD: float

    # OCR Settings
    TESSERACT_CMD: str
    LANG: str

    # Processing Settings
    BATCH_SIZE: int
    MAX_WORKERS: int
    INPUT_DIR: str
    OUTPUT_DIR: str
    TEMP_DIR: str

    # Logging
    LOG_LEVEL: str
    LOG_FILE: str

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"
        case_sensitive = True

    def get_database_url(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def get_input_dir(self) -> Path:
        return Path(self.INPUT_DIR)

    def get_output_dir(self) -> Path:
        return Path(self.OUTPUT_DIR)

    def get_temp_dir(self) -> Path:
        return Path(self.TEMP_DIR)

    def get_log_file(self) -> Path:
        return Path(self.LOG_FILE)

@lru_cache()
def get_settings() -> Settings:
    return Settings() 
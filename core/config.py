import os
from pathlib import Path, PurePath
from typing import Any, Dict, List, Optional
from pydantic import BaseSettings, validator
import cv2

PROJECT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR: str = os.path.dirname(PROJECT_DIR)


class Settings(BaseSettings):
    PROJECT_DIR: str = PROJECT_DIR
    BASE_DIR: str = BASE_DIR
    IMAGE_DIR: Path = Path(PROJECT_DIR) / "images"
    IMAGES: List[Path] = [file for file in IMAGE_DIR.glob("**/*") if file.is_file()]
    METHOD: Any = cv2.TM_CCOEFF_NORMED

    class Config:
        case_sensitive = True


settings = Settings()

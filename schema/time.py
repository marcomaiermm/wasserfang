from pydantic import BaseModel
from datetime import timedelta


class TimeModel(BaseModel):
    deltatime: timedelta = None
    time: str = "00:00"

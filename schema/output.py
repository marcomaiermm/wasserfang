from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta


class Output(BaseModel):
    base_text: str = "catched"
    status: str = "stopped"
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    elapsed: Optional[timedelta] = None

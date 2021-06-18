from pydantic import BaseModel


class StateManager(BaseModel):
    running: bool = False
    seconds: int = 0
    time: str = "00:00:00"
    catched: int = 0
    status: str = "stopped"

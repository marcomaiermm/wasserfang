import time
from datetime import timedelta
from schema.manager import StateManager
from utils.process import wow_process


class TimerThread:
    running: bool = True
    max_time: int = 0

    def timer(self, manager: StateManager):
        t = 0
        dtime = 0
        while 1:
            if not manager.running:
                break
            if wow_process():
                dtime = timedelta(seconds=t)

                manager.time = str(dtime)
                manager.seconds = t

                time.sleep(1)
                t += 1

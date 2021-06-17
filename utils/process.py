from typing import List

from psutil import Process
from win32 import win32gui, win32process


def get_active_process() -> str:
    pid: List[int] = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    name = ""
    try:
        name = Process(pid[-1]).name()
    except:
        pass
    return name


def wow_process() -> bool:
    b = False
    if get_active_process() == "WowClassic.exe":
        b = True
    return b

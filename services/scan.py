import pyautogui
import random
import time
from utils.image import scan
from utils.process import wow_process

from schema.manager import StateManager

class FishThread:
    def scan(self, manager: StateManager, initial: bool = False):
        last_x = 0
        last_y = 0
        blocked = 0
        catched = 0

        while 1:
            if not manager.running:
                break
            if wow_process():

                deviations = scan(scanning=initial)
                if not blocked:
                    last_x = 0
                    last_y = 0
                    pyautogui.press("1")
                    blocked = 1
                else:
                    b_x = 0
                    b_y = 0
                    if deviations[2] > 0:
                        b_x = int(deviations[1] / deviations[2])
                        b_y = int(deviations[0] / deviations[2])
                    if last_x > 0 and last_y > 0:
                        if last_x != b_x and last_y != b_y:
                            blocked = 0
                            if b_x < 1:
                                b_x = last_x
                            if b_y < 1:
                                b_y = last_y
                            pyautogui.moveTo(b_x, b_y + deviations[3][1], 0.2, pyautogui.easeOutQuad)
                            pyautogui.mouseDown(button="right")
                            pyautogui.mouseUp(button="right")
                            catched += 1
                            manager.catched = str(catched)
                            wait_time: float = random.uniform(1, 3)
                            time.sleep(wait_time)
                    last_x = b_x
                    last_y = b_y

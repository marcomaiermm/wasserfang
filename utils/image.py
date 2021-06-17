from typing import Any, List, Tuple
import cv2 as cv
import numpy as np
from PIL import ImageGrab
from datetime import datetime
from win32.win32gui import GetForegroundWindow, GetWindowRect

from core.config import settings


def templates():
    return [cv.cvtColor(cv.imread(x.__str__(), cv.IMREAD_UNCHANGED), cv.COLOR_BGR2HSV) for x in settings.IMAGES]


def grab_bobber() -> np.ndarray:
    bobber_img = cv.imread(settings.IMAGES[0].__str__(), cv.IMREAD_UNCHANGED)
    bobber_img = cv.cvtColor(bobber_img, cv.COLOR_BGR2GRAY)
    return bobber_img


def grab_screen() -> Tuple[Any]:
    # rect = [x,y,w,h]
    rect: Tuple[int] = GetWindowRect(GetForegroundWindow())
    area = (0, rect[1], rect[2], int(rect[3] * 0.77))
    screenshot = np.array(ImageGrab.grab())
    return (screenshot, area)


def generate_frames(image: np.ndarray) -> Tuple[Any]:
    frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    frame_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    frame_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return (frame, frame_hsv, frame_gray)


def mask_frames(frame_hsv: np.ndarray):
    h_min = np.array((0, 0, 253), np.uint8)
    h_max = np.array((255, 0, 255), np.uint8)
    return cv.inRange(frame_hsv, h_min, h_max)


def search():
    highest_val = -1
    screen = grab_screen()[0]
    frames = generate_frames(screen)
    bobbers = templates()
    results = []

    for bobber in bobbers:
        res = cv.matchTemplate(frames[1], bobber, settings.METHOD)
        _, max_val, _, max_loc = cv.minMaxLoc(res)
        if max_val > highest_val:
            results.append((max_val, max_loc))
    return results


def scan(scanning: bool = False):
    # if scanning:
    #     f: List[Any] = search()
    #     best: Tuple[Any] = max(f, key=itemgetter(0))
    #     x = best[1][0]
    #     y = best[1][1]
    #     screen = ImageGrab.grab(bbox=(x - 60, y - 68, x + 60, y + 68))
    # else:
    #     screen = grab_screen()
    # bobber = grab_bobber()

    grab_area = grab_screen()

    # max(res, key=itemgetter(0))
    # p_x = int(np.percentile(f_np_x, 50))
    # p_y = int(np.percentile(f_np_y, 50))

    # screen = ImageGrab.grab(bbox=(p_x, p_y, p_x + 200, p_y + 200))

    # screen_array = np.array(screen)

    frames = generate_frames(grab_area[0])
    mask = mask_frames(frames[1])
    moments = cv.moments(mask, 1)

    dM01 = moments["m01"]
    dM10 = moments["m10"]
    dArea = moments["m00"]

    # result = cv.matchTemplate(frames[0], bobber, cv.TM_CCOEFF_NORMED)111111111

    return (dM01, dM10, dArea, grab_area[1])
    # result = cv.matchTemplate(screen[0], bobber, cv.TM_CCOEFF_NORMED)
    # return result


def take_rect_screenshot(x: int, y: int):
    im = ImageGrab.grab(bbox=(x - 60, y - 68, x + 60, y + 68))
    im.save(f"images/bob{datetime.timestamp(datetime.now())}.png")

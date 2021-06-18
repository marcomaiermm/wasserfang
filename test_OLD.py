# if __name__ == "__main__":

from utils.image import search, generate_frames, grab_screen
from services.scanning_area import scan
from operator import itemgetter
import cv2


def sc():
    scan()


def loop():
    instance = cv2
    res = search()
    best = max(res, key=itemgetter(0))

    screen = grab_screen()[0]
    frame = generate_frames(screen)[2]
    # trows, tcols = grab_bobber().shape[:2]
    for r in res:
        x = r[1][0]
        y = r[1][1]

        instance.putText(
            frame, f"coeff. {r[0]}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA, False
        )
        instance.rectangle(frame, (x, y), (x + 100, y + 100), (0, 0, 255), 2)
    instance.imshow("output", frame)
    instance.waitKey()


scan(initial=False)

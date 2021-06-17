import threading
from schema import Output, Input
from services.scanning_area import scanning_area


class Worker:
    output = Output()
    input = Input()

    def main_thread(self):
        threading.Thread(target=scanning_area).start()

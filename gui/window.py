from threading import Thread
from kivy.lang import Builder
from kivymd.app import MDApp

from services.time import TimerThread
from services.scan import FishThread
from services.update import update_gui

from schema.manager import StateManager


class MainApp(MDApp):

    manager = StateManager()
    timer = None
    woker = None

    worker_thread = None
    timer_thread = None
    manager_thread = None

    running: bool = False

    def build(self):
        # Funktion für den Buld loader
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file("main.kv")

    def toggle(self):
        self.manager.running = not self.manager.running
        if self.manager.running:
            self.start_routine()

    def start_routine(self):

        # State reset
        self.reset()
        # State catching
        self.state.button_state = "Stop"
        self.root.ids.state_label.text = self.state.button_state

        self.manager.running = True

        # Threads starten
        self.manager_thread.start()
        self.timer_thread.start()
        self.worker_thread.start()

    def initialize(self):
        manager_args = (
            self.manager,
            self.root.ids.catched_label,
            self.root.ids.catch_label,
            self.root.ids.time_label,
            self.root.ids.time,
        )
        self.manager_thread = Thread(target=update_gui, args=manager_args)
        self.worker_thread = Thread(target=self.worker.scan, args=(self.manager,))
        self.timer_thread = Thread(target=self.timer.timer, args=(self.manager,))

        self.manager_thread.daemon = True
        self.timer_thread.daemon = True
        self.worker_thread.daemon = True

    def reset(self):
        self.state = State()
        self.manager = StateManager()
        self.timer = TimerThread()
        self.worker = FishThread()
        self.initialize()

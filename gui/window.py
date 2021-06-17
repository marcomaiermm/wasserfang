from kivy.lang import Builder
from kivymd.app import MDApp
from services.worker import Worker

STATUS = (
    "Stopped",
    "Fishing",
    "Looting",
    "Waiting",
)


class MainApp(MDApp):
    worker = Worker()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file("main.kv")

    def toggle_start(self):
        self.worker.main_thread()

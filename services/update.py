from schema.manager import StateManager


def update_gui(manager: StateManager, catched_label, status_label, time_elapsed, time_to_fish):
    while manager.running:
        if time_to_fish.text:
            if manager.seconds / 60 >= int(time_to_fish.text):
                manager.running = False
        catched_label.text = str(manager.catched)
        status_label.text = str(manager.status)
        time_elapsed.text = str(manager.time)

from utils.change_utils_for_printerv2 import adding_school_items, adding_chores_items
from datetime import datetime, time


while True:
    now = datetime.now()
    if now.hour == 7:
        if now.minute == 30:
            adding_school_items()
            adding_chores_items()
    if now.hour() == 8:
        task = school_to_do[0]
    time.sleep(60)

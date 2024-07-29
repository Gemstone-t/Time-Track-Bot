from pynput import mouse, keyboard
from datetime import datetime
import sqlite3
import threading
import time

# Initialize database
# conn = sqlite3.connect('time_tracker.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS activity_logs
#              (user_id TEXT, task TEXT, start_time TEXT, end_time TEXT)''')

current_task = None
start_time = None
activity_log = []

def log_activity(task):
    global activity_log, start_time, current_task
    end_time = datetime.now().isoformat()
    if current_task:
        # c.execute("INSERT INTO activity_logs (user_id, task, start_time, end_time) VALUES (?, ?, ?, ?)",
        #           ('user_123', current_task, start_time, end_time))
        # conn.commit()
        # activity_log.append((current_task, start_time, end_time))
        print(f'Task: {current_task}, Start: {start_time}, End: {end_time}\n')
    start_time = datetime.now().isoformat()
    current_task = task

def on_click(x, y, button, pressed):
    if pressed:
        log_activity("Mouse Activity")

def on_press(key):
    log_activity("Keyboard Activity")

def start_activity_monitor():
    global current_task, start_time

    with mouse.Listener(on_click=on_click) as mouse_listener, keyboard.Listener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()

if __name__ == "__main__":
    activity_thread = threading.Thread(target=start_activity_monitor)
    activity_thread.start()

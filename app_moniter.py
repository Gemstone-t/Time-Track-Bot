import psutil
import sqlite3
from datetime import datetime
import time
import threading
import os

conn = sqlite3.connect('time_tracker.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS activity_logs
             (user_id TEXT, task TEXT, start_time TEXT, end_time TEXT)''')

def get_active_window():

    # Get the process ID of
    pid = os.getpid()
    active_window_path = psutil.Process(pid).exe()
    print(pid)
    return str(active_window_path)

def track_applications():
    current_app = None
    start_time = None

    while True:
        active_app = get_active_window()
        if current_app != active_app:
            if current_app is not None:
                end_time = datetime.now().isoformat()
                c.execute("INSERT INTO activity_logs (user_id, task, start_time, end_time) VALUES (?, ?, ?, ?)",('user_123', current_app, start_time, end_time))
                conn.commit()
                print(f'Task: {current_app}, Start: {start_time}, End: {end_time}\n')
            current_app = active_app
            start_time = datetime.now().isoformat()
        time.sleep(1)

if __name__ == "__main__":
    app_thread = threading.Thread(target=track_applications)
    app_thread.start()

import csv
from datetime import datetime
import os

LOG_FILE = "activity_log.csv"

def log_activity(android_id, action):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Android ID", "Action"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), android_id, action])
    print(f"📄 Logged action: '{action}' for device {android_id}")

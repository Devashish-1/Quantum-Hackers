import csv
import random
import time
from datetime import datetime

LOG_FILE = "device_monitor_log.csv"
APPS = ["WhatsApp", "Instagram", "Chrome", "YouTube", "Gmail", "Spotify", "Maps", "Telegram", "Facebook", "Twitter"]
STATUSES = ["Active", "Background", "Killed"]

def generate_log_entry():
    app = random.choice(APPS)
    cpu = round(random.uniform(1, 85), 2)
    ram = round(random.uniform(100, 950), 2)
    battery = random.randint(5, 100)
    charging = random.choice(["Yes", "No"])
    status = random.choice(STATUSES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Smart alert system
    alerts = []
    if battery < 15:
        alerts.append("Low Battery")
    if ram > 500:
        alerts.append("High RAM Usage")
    if cpu > 70:
        alerts.append("High CPU Load")
    alert = "; ".join(alerts)
    
    return [timestamp, app, cpu, ram, battery, charging, status, alert]

def write_logs(interval=5):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Timestamp", "App", "CPU%", "RAM_MB", "Battery%", "Charging", "Status", "Alert"])
        while True:
            entry = generate_log_entry()
            writer.writerow(entry)
            print("Log added:", entry)
            time.sleep(interval)

if __name__ == "__main__":
    print(f"📲 Android log simulator running... Logging to {LOG_FILE}")
    write_logs()

import psutil
import time
import pandas as pd
from datetime import datetime
import os

LOG_FILE = "logs/system_log.csv"

def init_log_file():
    # If file doesn't exist, create it with headers
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=[
            'Timestamp', 'CPU%', 'Memory%', 'Disk%', 
            'Bytes_Sent(KB)', 'Bytes_Recv(KB)', 'Processes'
        ])
        df.to_csv(LOG_FILE, index=False)

def log_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters()
    processes = len(psutil.pids())

    sent_kb = round(net.bytes_sent / 1024, 2)
    recv_kb = round(net.bytes_recv / 1024, 2)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_row = {
        'Timestamp': timestamp,
        'CPU%': cpu,
        'Memory%': memory,
        'Disk%': disk,
        'Bytes_Sent(KB)': sent_kb,
        'Bytes_Recv(KB)': recv_kb,
        'Processes': processes
    }

    df = pd.DataFrame([log_row])
    df.to_csv(LOG_FILE, mode='a', header=not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0, index=False)
    print(f"🔄 Logged at {timestamp}: CPU={cpu}%, RAM={memory}%, Disk={disk}%")

if __name__ == "__main__":
    init_log_file()
    print("✅ Monitoring started... Press Ctrl+C to stop.")
    try:
        while True:
            log_system_metrics()
            time.sleep(5)
    except KeyboardInterrupt:
        print("🛑 Monitoring stopped.")

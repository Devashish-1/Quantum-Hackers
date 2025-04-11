import socket
import os
import time
import subprocess
from win10toast import ToastNotifier

# Configuration
receiver_ip = '127.0.0.1'
receiver_port = 5001
buffer_size = 4096
received_filename = "received_file.txt"
signature_file = "signatures.txt"
android_notification_message = "🚨 Your system is affected by virus!"

# Setup Windows notifier
notifier = ToastNotifier()

# Get Desktop path
def get_desktop_path():
    possible_paths = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop"),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("❌ Desktop path not found.")

desktop_path = get_desktop_path()
file_path = os.path.join(desktop_path, received_filename)
signature_path = os.path.join(os.path.dirname(__file__), signature_file)

# Load virus signatures
def load_signatures(path):
    with open(path, 'r') as f:
        return [line.strip().lower() for line in f if line.strip()]

# Scan file
def scan_file(file_path, signatures):
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read().lower()
            return [sig for sig in signatures if sig in content]
    except Exception as e:
        print(f"❌ Error scanning file: {e}")
        return []

# Optional CMD logging
def execute_cmd_command():
    cmd_command = "echo [!] Virus handling triggered >> C:\\virus_alert_log.txt"
    try:
        subprocess.run(cmd_command, shell=True)
    except Exception as e:
        print(f"❌ CMD Execution Failed: {e}")

# Windows Notifications (10 toasts)
def send_windows_toasts():
    for i in range(1, 11):
        notifier.show_toast("🚨 VIRUS ALERT", f"ALERT {i}/10: Malicious file detected!", duration=3)
        time.sleep(2)

# Android Notifications via ADB
def send_android_notifications():
    print("📲 Sending 10 Android alerts via ADB...")
    try:
        os.system('adb shell input keyevent 82')  # Wake screen
        for i in range(1, 11):
            os.system(f'adb shell cmd notification post -S bigtext -t "VIRUS ALERT {i}/10" "com.android.systemui" "{android_notification_message}"')
            print(f"✅ Android Notification {i}/10 sent.")
            time.sleep(2)
    except Exception as e:
        print(f"❌ ADB Notification Failed: {e}")

# Start receiver socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((receiver_ip, receiver_port))
s.listen(1)

print(f"📥 Listening on {receiver_ip}:{receiver_port}...")
client_socket, client_addr = s.accept()
print(f"✅ Connected to sender: {client_addr}")

# Receive file
with open(file_path, "wb") as file:
    while True:
        bytes_read = client_socket.recv(buffer_size)
        if not bytes_read:
            break
        file.write(bytes_read)

print(f"📄 File saved to Desktop as '{received_filename}'")

# Scan and alert
signatures = load_signatures(signature_path)
matches = scan_file(file_path, signatures)

if matches:
    print("🚨 Virus Detected! Matched Signatures:")
    for sig in matches:
        print(f" - {sig}")

    execute_cmd_command()
    send_windows_toasts()
    send_android_notifications()
else:
    print("✅ File is clean. No virus signatures matched.")

client_socket.close()
s.close()

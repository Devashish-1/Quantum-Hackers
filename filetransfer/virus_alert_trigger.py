import os
import subprocess
import time

# === CONFIGURATION ===
cmd_command = "echo ALERT: CMD executed for virus handling."  # Example CMD command
android_notification_message = "🚨 ALERT: Malicious file received on PC!"

# === STEP 1: Run CMD command on PC ===
def execute_cmd_command():
    print("🖥️ Running CMD command...")
    try:
        result = subprocess.run(cmd_command, shell=True, capture_output=True, text=True)
        print("✅ CMD Output:", result.stdout.strip())
    except Exception as e:
        print(f"❌ CMD Execution Failed: {e}")

# === STEP 2: Send Android Notification via ADB ===
def send_android_notification_via_adb():
    print("📲 Sending ADB notification to connected Android device...")
    try:
        os.system('adb shell input keyevent 82')  # Wake screen
        time.sleep(1)
        os.system(f'adb shell cmd notification post -S bigtext -t "Virus Alert" "com.android.systemui" "{android_notification_message}"')
        print("✅ Android notification sent.")
    except Exception as e:
        print(f"❌ ADB Notification Failed: {e}")

if __name__ == "__main__":
    execute_cmd_command()
    time.sleep(2)
    send_android_notification_via_adb()

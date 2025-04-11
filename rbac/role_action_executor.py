import subprocess

def get_connected_devices():
    result = subprocess.check_output(["adb", "devices"]).decode()
    lines = result.strip().split('\n')[1:]
    return [line.split('\t')[0] for line in lines if 'device' in line]

def get_device_info(device_id):
    android_id = subprocess.check_output(["adb", "-s", device_id, "shell", "settings", "get", "secure", "android_id"]).decode().strip()
    model = subprocess.check_output(["adb", "-s", device_id, "shell", "getprop", "ro.product.model"]).decode().strip()
    manufacturer = subprocess.check_output(["adb", "-s", device_id, "shell", "getprop", "ro.product.manufacturer"]).decode().strip()
    version = subprocess.check_output(["adb", "-s", device_id, "shell", "getprop", "ro.build.version.release"]).decode().strip()

    print(f"📱 Device Info:\nModel: {model}\nManufacturer: {manufacturer}\nAndroid Version: {version}\nAndroid ID: {android_id}\n")
    
    return {"device_id": device_id, "android_id": android_id, "model": model}

# Test run only if this script is executed directly
if __name__ == "__main__":
    devices = get_connected_devices()
    if not devices:
        print("⚠️ No Android device connected.")
    else:
        for dev in devices:
            get_device_info(dev)

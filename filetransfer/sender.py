import socket
import os

receiver_ip = "127.0.0.1"
receiver_port = 5001
buffer_size = 4096

file_to_send = "file.txt"  # Copy either normal_text.txt or malicious_text.txt as file.txt
file_path = os.path.join(os.path.dirname(__file__), file_to_send)

if not os.path.exists(file_path):
    print(f"❌ Error: '{file_to_send}' not found!")
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"🔗 Connecting to {receiver_ip}:{receiver_port}...")
s.connect((receiver_ip, receiver_port))
print("✅ Connected!")

with open(file_path, "rb") as file:
    while True:
        bytes_read = file.read(buffer_size)
        if not bytes_read:
            break
        s.sendall(bytes_read)

print(f"📤 File '{file_to_send}' sent successfully!")
s.close()

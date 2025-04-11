import os
import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet

# Encrypt a file using the encryption key
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        plaintext = file.read()
    encrypted_data = fernet.encrypt(plaintext)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Main function to encrypt files with a manually set encryption key
def encrypt_files_with_manual_key():
    # Manually enter the encryption key
    key = input("Enter encryption key (32 bytes in length): ").encode()
    if len(key) != 32:
        print("Invalid key length. Key must be 32 bytes in length.")
        return

    # Get the target directory using a file dialog
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    target_directory = filedialog.askdirectory(title="Select Target Directory")

    # Encrypt files in the selected directory
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        if os.path.isfile(file_path):  # Encrypt only files, not directories
            encrypt_file(file_path, key)

    print("Files encrypted successfully.")

# Example usage: Run the encryption process
if __name__ == "__main__":
    encrypt_files_with_manual_key()

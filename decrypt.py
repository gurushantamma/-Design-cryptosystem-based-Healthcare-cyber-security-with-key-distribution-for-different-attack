from tkinter import messagebox

from cryptography.fernet import Fernet

def decrypt_file():
    with open("C:/healthblockchain/encryption/key.key", "rb") as key_file:
        key = key_file.read()

    with open("C:/healthblockchain/data/encrypted_record.txt", "rb") as f:
        encrypted = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)

    print("Decrypted data:\n", decrypted.decode())
    messagebox.showinfo("Healthcare",decrypted.decode())

if __name__ == "__main__":
    decrypt_file()

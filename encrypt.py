from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("C:/healthblockchain/encryption/key.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_file():
    with open("C:/healthblockchain/data/record.txt", "rb") as f:
        data = f.read()

    key = generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open("C:/healthblockchain/data/encrypted_record.txt", "wb") as f:
        f.write(encrypted)

    print("Encrypted data saved.")
    return encrypted.decode()

if __name__ == "__main__":
    encrypt_file()

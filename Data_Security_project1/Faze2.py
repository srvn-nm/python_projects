import argparse
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


def generate_key(password):

    # Derive a key from the password using PBKDF2
    salt = b'salt_'  # Salt value to make the key unique
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Length of the key
        salt=salt,
        iterations=100000,  # Number of iterations
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    f = Fernet(key)
    encrypted_data = f.encrypt(data)

    with open(f"{file_path}.encrypted", 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    with open(f"{file_path[:-10]}_decrypted.txt", 'wb') as file:
        file.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="File Encryption and Decryption Tool")
    parser.add_argument("mode", type=int, choices=[1, 2], help="Select mode (1: Encryption, 2: Decryption)")
    parser.add_argument("file_path", help="Path of the file")
    parser.add_argument("password", help="Password for encryption/decryption")

    args = parser.parse_args()
    key = generate_key(args.password.encode())

    if args.mode == 1:
        encrypt_file(args.file_path, key)
        print("File encrypted successfully.")
    elif args.mode == 2:
        decrypt_file(args.file_path, key)
        print("File decrypted successfully.")
    else:
        print("Invalid mode. Please select 1 for encryption or 2 for decryption.")

if __name__ == "__main__":
    main()

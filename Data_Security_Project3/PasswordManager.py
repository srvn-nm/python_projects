import argparse
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import hashlib


def derive_key(password):
    salt = b'salt_1234'  # مقدار تصادفی برای استفاده در تولید کلید
    kdf = PBKDF2HMAC(
        algorithm=algorithms.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # تعداد تکرارها برای تقویت امنیت
    )
    key = urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt(password, plaintext):
    key = derive_key(password)
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return urlsafe_b64encode(ciphertext)

def decrypt(password, ciphertext):
    key = derive_key(password)
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(urlsafe_b64decode(ciphertext)) + decryptor.finalize()
    return plaintext.decode()

def save_passwords(passwords, password):
    encrypted_passwords = encrypt(password, json.dumps(passwords))
    with open('passwords.txt', 'wb') as file:
        file.write(encrypted_passwords)

def load_passwords(password):
    if not os.path.exists('passwords.txt'):
        return {}
    with open('passwords.txt', 'rb') as file:
        encrypted_passwords = file.read()
    try:
        decrypted_passwords = decrypt(password, encrypted_passwords)
        return json.loads(decrypted_passwords)
    except Exception as e:
        print(f"Error decrypting passwords: {e}")
        return {}

def main():
    parser = argparse.ArgumentParser(description="Password Manager CLI Tool")
    parser.add_argument("--newpass", help="Create a new password", action="store_true")
    parser.add_argument("--showpass", help="Show all passwords", action="store_true")
    parser.add_argument("--sel", help="Select and show a password by name")
    parser.add_argument("--update", help="Update a password by name")
    parser.add_argument("--dell", help="Delete a password by name")
    parser.add_argument("--c", help="Comment for the new password")
    parser.add_argument("--key", help="User simple password")

    args = parser.parse_args()

    if args.newpass:
        name = input("Enter a name for the new password: ")
        comment = input("Enter a comment for the new password: ")
        password = input("Enter a simple password: ")
        key = input("Enter the user simple password: ")

        # Generate a complex password based on the simple password
        complex_password = generate_complex_password(password)

        # Load existing passwords
        passwords = load_passwords(key)

        # Add the new password to the password manager
        passwords[name] = {"password": complex_password, "comment": comment}

        # Save the updated passwords
        save_passwords(passwords, key)
        print("Password created successfully!")

    elif args.showpass:
        key = input("Enter the user simple password: ")
        passwords = load_passwords(key)
        print("List of passwords:")
        for name, info in passwords.items():
            print(f"Name: {name}, Password: {info['password']}, Comment: {info['comment']}")

    elif args.sel:
        key = input("Enter the user simple password: ")
        passwords = load_passwords(key)
        selected_name = args.sel
        if selected_name in passwords:
            print(f"Name: {selected_name}, Password: {passwords[selected_name]['password']}, Comment: {passwords[selected_name]['comment']}")
        else:
            print(f"Password with name '{selected_name}' not found.")

    elif args.update:
        key = input("Enter the user simple password: ")
        passwords = load_passwords(key)
        update_name = args.update
        if update_name in passwords:
            new_password = input("Enter the new password: ")
            complex_password = generate_complex_password(new_password)
            passwords[update_name]['password'] = complex_password
            save_passwords(passwords, key)
            print(f"Password with name '{update_name}' updated successfully!")
        else:
            print(f"Password with name '{update_name}' not found.")

    elif args.dell:
        key = input("Enter the user simple password: ")
        passwords = load_passwords(key)
        delete_name = args.dell
        if delete_name in passwords:
            del passwords[delete_name]
            save_passwords(passwords, key)
            print(f"Password with name '{delete_name}' deleted successfully!")
        else:
            print(f"Password with name '{delete_name}' not found.")

def generate_complex_password(simple_password):
    # Derive a key from the simple password using a key derivation function
    key = hashlib.sha256(simple_password.encode()).digest()

    # Use AES in CFB mode to encrypt a fixed value (e.g., '123!') to create the complex password
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\x00' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    complex_password = encryptor.update(b'123!') + encryptor.finalize()

    # Convert the complex password to a base64-encoded string
    return base64.urlsafe_b64encode(complex_password).decode()

if __name__ == "__main__":
    main()

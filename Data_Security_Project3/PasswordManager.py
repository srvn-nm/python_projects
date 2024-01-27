import argparse
import base64
import json
import os
# noinspection PyCompatibility
import secrets
# from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Function to derive a key from a password using PBKDF2HMAC
# noinspection PyGlobalUndefined,PyCompatibility
def derive_key(password):
    key = b''
    salt = os.urandom(16)  # Generate a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=16,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    if isinstance(password, bytes):
        key = base64.urlsafe_b64encode(kdf.derive(password))
    elif isinstance(password, int):
        key = base64.urlsafe_b64encode(kdf.derive(str(password).encode('utf-8')))
    elif isinstance(password, str):  # handle case when password is of str type
        key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
    else:
        print(f"Unhandled password type: {type(password)}")
    return key, salt


# Function to encrypt plaintext using AES in CFB mode
# noinspection PyShadowingNames
def encrypt_data(data, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
    return base64.urlsafe_b64encode(ciphertext).decode()
    #
    # cipher_suite = Fernet(key)
    # encrypted_data = cipher_suite.encrypt(data.encode())
    # return encrypted_data


# Function to decrypt ciphertext using AES in CFB mode
# noinspection PyShadowingNames
def decrypt_data(encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(base64.urlsafe_b64decode(encrypted_data)) + decryptor.finalize()
    return plaintext.decode()
    # cipher_suite = Fernet(key)
    # decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    # return decrypted_data


# Function to save a password to a file along with its metadata
# noinspection PyShadowingNames,PyCompatibility
def save_password(name, password, comment, key):
    with open('passwords.txt', 'a') as file:
        encrypted_password = encrypt_data(password, key)
        file.write(f"{name}:{encrypted_password}:{comment}\n")


# Function to load passwords from a file and decrypt them
# noinspection PyShadowingNames
def load_passwords(key):
    with open('passwords.txt', 'r') as file:
        encrypted_passwords = json.load(file)
    passwords = {name: (decrypt_data(password.encode(), key), comment.rstrip()) for name, (password, comment) in
                 encrypted_passwords.items()}
    return passwords


# Function to save passwords to a file
def save_passwords(passwords, key):
    encrypted_passwords = {name: (encrypt_data(password, key), comment) for name, (password, comment) in
                           passwords.items()}
    with open('passwords.txt', 'w') as file:
        json.dump(encrypted_passwords, file)


# Main function to handle command-line arguments
# noinspection PyCompatibility,PyShadowingNames
def main():
    parser = argparse.ArgumentParser(description='Password Management Tool')
    subparsers = parser.add_subparsers(dest='command')

    newpass_parser = subparsers.add_parser('newpass', help='Create a new password')
    newpass_parser.add_argument('name', type=str, help='Name of the password')
    newpass_parser.add_argument('-c', '--comment', type=str, help='Comment for the password', nargs='*')
    newpass_parser.add_argument('--key', type=str, help='Simple password for encryption')

    sel_parser = subparsers.add_parser('sel', help='Select a specific password to view')
    sel_parser.add_argument('name', type=str, help='Name of the password to view')

    update_parser = subparsers.add_parser('update', help='Update an existing password')
    update_parser.add_argument('name', type=str, help='Name of the password to update')

    del_parser = subparsers.add_parser('del', help='Delete an existing password')
    del_parser.add_argument('name', type=str, help='Name of the password to delete')

    showpass_parser = subparsers.add_parser('showpass', help='Show all passwords')
    showpass_parser.add_argument('--key', type=str, help='Simple password for decryption')

    args = parser.parse_args()

    if args.command == 'newpass':
        password = generate_complex_password(simple_password=args.key, name=args.name, comment=args.comment, key=args.key)
        save_password(name=args.name, key=args.key, comment=args.comment, password=str(password))
    elif args.command == 'showpass':
        saved_passwords = load_passwords(args.key)
        for name in saved_passwords:
            print(name)
    elif args.command == 'sel':
        saved_passwords = load_passwords(args.key)
        if args.name in saved_passwords:
            print(f"Password: {saved_passwords[args.name][0]}")
            print(f"Comment: {saved_passwords[args.name][1]}")
    elif args.command == 'update':
        saved_passwords = load_passwords(args.key)
        if args.name in saved_passwords:
            updated_password = input("Enter the updated password: ")
            updated_comment = input("Enter the updated comment: ")
            saved_passwords[args.name] = (updated_password, updated_comment)
            save_passwords(saved_passwords, args.key)
            print(f"Password '{args.name}' updated successfully!")
        else:
            print(f"No password found with the name '{args.name}'")
    elif args.command == 'del':
        saved_passwords = load_passwords(args.key)
        if args.name in saved_passwords:
            del saved_passwords[args.name]
            save_passwords(saved_passwords, args.key)
            print(f"Password '{args.name}' deleted successfully!")
        else:
            print(f"No password found with the name '{args.name}'")


# Function to generate a complex password, encrypt it, and save to file
# noinspection PyShadowingNames
def generate_complex_password(simple_password, name, comment, key):
    # Generate a complex password based on the simple password
    random_suffix = secrets.token_hex(4)  # Generate a random hexadecimal string of length 4
    complex_password = simple_password.upper() + random_suffix

    # Derive key and salt
    derived_key, salt = derive_key(key)
    print(derived_key)

    # Make sure both salt and complex password are string before concatenation
    data_to_encrypt = str(salt) + complex_password
    encrypted_password = encrypt_data(key=derived_key, data=data_to_encrypt)

    # Save the generated password along with its metadata to a file
    save_password(name, str(encrypted_password), comment, key)

    return encrypted_password


# Entry point of the script
if __name__ == "__main__":
    main()

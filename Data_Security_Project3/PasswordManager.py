import argparse
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os
import secrets


# Function to derive a key from a password using PBKDF2HMAC
# noinspection PyGlobalUndefined
def derive_key(password):
    key = b''
    print("derive")
    print(type(password))
    salt = os.urandom(16)  # Generate a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    if isinstance(password, bytes):
        key = base64.urlsafe_b64encode(kdf.derive(password))
    elif isinstance(password, int):
        key = base64.urlsafe_b64encode(kdf.derive(str(password).encode('utf-8')))
    return key, salt


# Function to encrypt plaintext using AES in CFB mode
# noinspection PyShadowingNames
def encrypt(password, plaintext):
    key, salt = derive_key(password)
    # Ensure the key is the correct size (e.g., 32 bytes for a 256-bit key)
    key = key[:32]
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return base64.urlsafe_b64encode(ciphertext).decode()


# Function to decrypt ciphertext using AES in CFB mode
# noinspection PyShadowingNames
def decrypt(password, ciphertext):
    key, salt = derive_key(password)
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(base64.urlsafe_b64decode(ciphertext)) + decryptor.finalize()
    return plaintext.decode()


# Function to save a password to a file along with its metadata
# noinspection PyShadowingNames
def save_password_to_file(name, encrypted_password, comment, key):
    # Load existing passwords from the file
    passwords = load_passwords_from_file(key)

    # Add the new password to the password manager
    passwords[name] = {"password": encrypted_password, "comment": comment}

    # Save the updated passwords to the file
    save_passwords_to_file(passwords, key)


# Function to load passwords from a file and decrypt them
# noinspection PyShadowingNames
def load_passwords_from_file(key):
    try:
        with open('passwords.txt', 'r') as file:
            encrypted_passwords = file.read()
            decrypted_passwords = decrypt(key, encrypted_passwords)
            return json.loads(decrypted_passwords)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Function to save encrypted passwords to a file
# noinspection PyShadowingNames
def save_passwords_to_file(passwords, key):
    encrypted_passwords = encrypt(key, json.dumps(passwords))
    with open('passwords.txt', 'w') as file:
        file.write(encrypted_passwords)


# Main function to handle command-line arguments
# noinspection PyCompatibility,PyShadowingNames
def main():
    parser = argparse.ArgumentParser(description="Password Manager CLI Tool")
    parser.add_argument("-newpass", nargs=1, type=str, help="Create a new password")
    parser.add_argument("-showpass", help="Show all passwords")
    parser.add_argument("-sel", nargs=1, type=str, help="Select and show a password by name")
    parser.add_argument("-update", nargs=1, type=str, help="Update a password by name")
    parser.add_argument("-dell", nargs=1, type=str, help="Delete a password by name")
    parser.add_argument("-c", nargs='*', type=str, help="Comment for the new password")
    parser.add_argument("-key", nargs=1, type=str, help="User simple password")
    parser.add_argument("-generate_passwords", nargs=1, type=str, help="Generate 10,000 passwords")

    args = parser.parse_args()
    key = args.key[0]

    if args.newpass:
        name = args.newpass[0]
        comment = ' '.join(args.c)
        password = name

        # Generate a complex password based on the simple password
        print("if")
        print(type(key))
        complex_password = generate_complex_password(password, name, comment, key)

        print(f"Generated Password: {complex_password}")
        print("Password created successfully!")

    elif args.showpass:
        show_passwords(key)

    elif args.sel:
        selected_name = args.sel
        show_selected_password(key, selected_name)

    elif args.update:
        update_name = args.update
        update_password(key, update_name)

    elif args.dell:
        delete_name = args.dell
        delete_password(key, delete_name)

    elif args.generate_passwords:
        simplePassword = args.generate_passwords
        generate_10000_passwords(key, simplePassword)
        print("Generated 10,000 passwords successfully!")


# Function to generate a complex password, encrypt it, and save to file
# noinspection PyShadowingNames
def generate_complex_password(simple_password, name, comment, key):
    # Generate a complex password based on the simple password
    random_suffix = secrets.token_hex(4)  # Generate a random hexadecimal string of length 4
    complex_password = simple_password.upper() + random_suffix

    # Derive key and salt
    print("generate")
    print(type(key))
    derived_key, salt = derive_key(key)

    # Encrypt the complex password using AES with the derived key and salt
    encrypted_password = encrypt(derived_key, salt + complex_password.encode('utf-8'))

    # Save the generated password along with its metadata to a file
    save_password_to_file(name, encrypted_password, comment, key)

    return encrypted_password


# Function to generate 10,000 passwords based on the provided simple password
# noinspection PyCompatibility,PyShadowingNames
def generate_10000_passwords(key, simple_password):
    # Open a file to write all passwords
    with open('all_passwords.txt', 'w') as file:
        for i in range(10000):
            name = f"Generated_Password_{i}"
            comment = f"Generated Password {i} for testing"
            key = key

            # Generate complex password and write to the file
            complex_password = generate_complex_password(simple_password, name, comment, key)
            file.write(f"Name: {name}, Password: {complex_password}, Comment: {comment}\n")

    print("All 10,000 passwords generated and saved in 'all_passwords.txt'")


# Function to show all passwords
# noinspection PyCompatibility,PyShadowingNames
def show_passwords(key):
    passwords = load_passwords_from_file(key)
    print("List of passwords:")
    for name, info in passwords.items():
        print(f"Name: {name}, Password: {info['password']}, Comment: {info['comment']}")


# Function to show a selected password
# noinspection PyCompatibility,PyShadowingNames
def show_selected_password(key, selected_name):
    passwords = load_passwords_from_file(key)
    if selected_name in passwords:
        print(
            f"Name: {selected_name}, Password: {passwords[selected_name]['password']}, Comment: {passwords[selected_name]['comment']}")
    else:
        print(f"Password with name '{selected_name}' not found.")


# Function to update a password
# noinspection PyCompatibility,PyShadowingNames
def update_password(key, update_name):
    passwords = load_passwords_from_file(key)
    if update_name in passwords:
        new_password = input("Enter the new password: ")
        generate_complex_password(new_password, update_name, passwords[update_name]['comment'], key)
        print(f"Password with name '{update_name}' updated successfully!")
    else:
        print(f"Password with name '{update_name}' not found.")


# Function to delete a password
# noinspection PyCompatibility,PyShadowingNames
def delete_password(key, delete_name):
    passwords = load_passwords_from_file(key)
    if delete_name in passwords:
        del passwords[delete_name]
        save_passwords_to_file(passwords, key)
        print(f"Password with name '{delete_name}' deleted successfully!")
    else:
        print(f"Password with name '{delete_name}' not found.")


# Entry point of the script
if __name__ == "__main__":
    main()

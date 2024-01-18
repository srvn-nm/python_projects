import argparse
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os

# Function to derive a key from a password using PBKDF2HMAC
def derive_key(password):
    salt = b'salt_1234'
    kdf = PBKDF2HMAC(
        algorithm=algorithms.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Function to encrypt plaintext using AES in CFB mode
def encrypt(password, plaintext):
    key = derive_key(password)
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return base64.urlsafe_b64encode(ciphertext).decode()

# Function to decrypt ciphertext using AES in CFB mode
def decrypt(password, ciphertext):
    key = derive_key(password)
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(base64.urlsafe_b64decode(ciphertext)) + decryptor.finalize()
    return plaintext.decode()

# Function to save a password to a file along with its metadata
def save_password_to_file(name, encrypted_password, comment, key):
    # Load existing passwords from the file
    passwords = load_passwords_from_file(key)

    # Add the new password to the password manager
    passwords[name] = {"password": encrypted_password, "comment": comment}

    # Save the updated passwords to the file
    save_passwords_to_file(passwords, key)

# Function to load passwords from a file and decrypt them
def load_passwords_from_file(key):
    try:
        with open('passwords.txt', 'r') as file:
            encrypted_passwords = file.read()
            decrypted_passwords = decrypt(key, encrypted_passwords)
            return json.loads(decrypted_passwords)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save encrypted passwords to a file
def save_passwords_to_file(passwords, key):
    encrypted_passwords = encrypt(key, json.dumps(passwords))
    with open('passwords.txt', 'w') as file:
        file.write(encrypted_passwords)

# Main function to handle command-line arguments
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
        complex_password = generate_complex_password(password, name, comment, key)

        print(f"Generated Password: {complex_password}")
        print("Password created successfully!")

    elif args.showpass:
        key = input("Enter the user simple password: ")
        show_passwords(key)

    elif args.sel:
        key = input("Enter the user simple password: ")
        selected_name = args.sel
        show_selected_password(key, selected_name)

    elif args.update:
        key = input("Enter the user simple password: ")
        update_name = args.update
        update_password(key, update_name)

    elif args.dell:
        key = input("Enter the user simple password: ")
        delete_name = args.dell
        delete_password(key, delete_name)

# Function to generate a complex password, encrypt it, and save to file
def generate_complex_password(simple_password, name, comment, key):
    # Generate a complex password based on the simple password
    complex_password = simple_password.upper() + "123!"

    # Encrypt the complex password using AES
    encrypted_password = encrypt(key, complex_password)

    # Save the generated password along with its metadata to a file
    save_password_to_file(name, encrypted_password, comment, key)

    return encrypted_password

# Function to show all passwords
def show_passwords(key):
    passwords = load_passwords_from_file(key)
    print("List of passwords:")
    for name, info in passwords.items():
        print(f"Name: {name}, Password: {info['password']}, Comment: {info['comment']}")

# Function to show a selected password
def show_selected_password(key, selected_name):
    passwords = load_passwords_from_file(key)
    if selected_name in passwords:
        print(f"Name: {selected_name}, Password: {passwords[selected_name]['password']}, Comment: {passwords[selected_name]['comment']}")
    else:
        print(f"Password with name '{selected_name}' not found.")

# Function to update a password
def update_password(key, update_name):
    passwords = load_passwords_from_file(key)
    if update_name in passwords:
        new_password = input("Enter the new password: ")
        complex_password = generate_complex_password(new_password, update_name, passwords[update_name]['comment'], key)
        print(f"Password with name '{update_name}' updated successfully!")
    else:
        print(f"Password with name '{update_name}' not found.")

# Function to delete a password
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

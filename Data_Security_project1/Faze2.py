from cryptography.fernet import Fernet

def generate_key(password):
    # تولید کلید براساس گذرواژه
    return Fernet.generate_key()

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
    mode = int(input("Please choose mode: (1: Encryption, 2: Decryption): "))

    password = input("Enter password for encryption/decryption: ")
    key = generate_key(password.encode())

    if mode == 1:
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif mode == 2:
        file_path = input("Enter the path of the file to decrypt: ")
        decrypt_file(file_path, key)
        print("File decrypted successfully.")
    else:
        print("Invalid mode. Please select 1 for encryption or 2 for decryption.")

if __name__ == "__main__":
    main()

import base64
import json
import random
import secrets
import string
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PasswordManager:
    def __init__(self, key):
        self.key = key
        self.passwords = {}

    def encrypt(self, data):
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(data.encode())
        return cipher_text

    def decrypt(self, cipher_text):
        cipher_suite = Fernet(self.key)
        plain_text = cipher_suite.decrypt(cipher_text).decode()
        return plain_text

    def save_password(self, name, password, comment):
        encrypted_password = self.encrypt(password)
        self.passwords[name] = {"password": encrypted_password, "comment": comment}
        with open('passwords.txt', 'a') as file:
            file.write(f"{name}:{encrypted_password}:{comment}\n")

    def get_password(self, name):
        if name in self.passwords:
            return self.decrypt(self.passwords[name]["password"]), self.passwords[name]["comment"]
        else:
            return None, None

    def get_all_passwords(self):
        passwords = {}
        with open('passwords.txt', 'r') as file:
            for line in file:
                name, encrypted_password, comment = line.strip().split(':')
                passwords[name] = {"password": encrypted_password, "comment": comment}
        return passwords

    def update_password(self, name, new_password):
        passwords = self.get_all_passwords()
        if name in passwords:
            if name in self.passwords:
                encrypted_password = self.encrypt(new_password)
                self.passwords[name]["password"] = encrypted_password
                new_comment = passwords[name]["comment"]
                with open('passwords.txt', 'w') as file:
                    for n, p, c in [(n, p["password"], p["comment"]) for n, p in passwords.items()]:
                        file.write(f"{n}:{p}:{c}\n")
                return True
            else:
                return False
        else:
            return False

    def delete_password(self, name):
        passwords = self.get_all_passwords()
        if name in passwords:
            if name in self.passwords:
                del self.passwords[name]
                with open('passwords.txt', 'w') as file:
                    for n, p, c in [(n, p["password"], p["comment"]) for n, p in passwords.items() if n != name]:
                        file.write(f"{n}:{p}:{c}\n")
                return True
            else:
                return False
        else:
            return False

    def show_passwords(self):
        return list(self.passwords.keys())

    def generate_secure_password(self):
        min_length = 12
        max_length = 20
        length = random.randint(min_length, max_length)

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    def generate_new_passwords(self):
        try:
            fixed_count = 10000
            passwords = [self.generate_secure_password() for _ in range(fixed_count)]

            with open('test.txt', 'w') as file:
                for password in passwords:
                    file.write(f"{password}\n")

            messagebox.showinfo("Success", f"{fixed_count} secure passwords generated and saved to 'test.txt' successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


class PasswordManagerGUI:
    def __init__(self):
        self.key_label = None
        self.key_entry = None
        self.key_button = None
        self.root = tk.Tk()
        self.root.title("Password Manager")

        self.password_manager = None
        self.create_key_entry()
        self.create_password_manager()

    def create_key_entry(self):
        self.key_label = tk.Label(self.root, text="Enter a simple password:")
        self.key_entry = tk.Entry(self.root, show="*")
        self.key_button = tk.Button(self.root, text="Create Key", command=self.create_password_manager)

        self.key_label.pack(pady=10)
        self.key_entry.pack(pady=10)
        self.key_button.pack(pady=10)

    def create_password_manager(self):
        key_password = self.key_entry.get()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            salt=b'salt',
            iterations=100000,
            length=32,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(key_password.encode()))
        self.password_manager = PasswordManager(key)
        self.show_password_manager_menu()

    def show_password_manager_menu(self):
        self.root.destroy()
        menu = PasswordManagerMenu(self.password_manager)
        menu.show_menu()


class PasswordManagerMenu:
    def __init__(self, password_manager):
        self.password_manager = password_manager
        self.menu = tk.Tk()
        self.menu.title("Password Manager Menu")

        self.menu_options = [
            ("Create New Password", self.show_new_password_entry),
            ("Show Passwords", self.show_passwords),
            ("Get Password", self.show_get_password_entry),
            ("Update Password", self.show_update_password_entry),
            ("Delete Password", self.show_delete_password_entry),
            ("Generate Secure Passwords", self.generate_new_passwords),
            ("Quit", self.quit_menu)
        ]

        self.create_menu_buttons()

    def create_menu_buttons(self):
        for option, command in self.menu_options:
            button = tk.Button(self.menu, text=option, command=command)
            button.pack(pady=10)

    def show_new_password_entry(self):
        entry = tk.Toplevel(self.menu)
        entry.title("Create New Password")

        name_label = tk.Label(entry, text="Enter password name:")
        name_entry = tk.Entry(entry)
        comment_label = tk.Label(entry, text="Enter comment:")
        comment_entry = tk.Entry(entry)

        name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        comment_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        comment_entry.grid(row=1, column=1, padx=10, pady=5)

        create_button = tk.Button(entry, text="Create Password",
                                  command=lambda: self.create_password(entry, name_entry.get(), comment_entry.get()))
        create_button.grid(row=2, column=0, columnspan=2, pady=10)

    def create_password(self, entry, name, comment):
        if not name:
            messagebox.showerror("Error", "Invalid input. Please enter a name.")
            return

        length = random.randint(len(name), 2 * len(name))
        password = self.password_manager.generate_secure_password()
        self.password_manager.save_password(name, password, comment)
        messagebox.showinfo("Success", f"Password '{name}' created successfully.\nPassword: {password}")
        entry.destroy()

    def show_passwords(self):
        passwords = self.password_manager.show_passwords()
        if passwords:
            messagebox.showinfo("Passwords", "\n".join(passwords))
        else:
            messagebox.showinfo("Passwords", "No passwords found.")

    def show_get_password_entry(self):
        entry = tk.Toplevel(self.menu)
        entry.title("Get Password")

        name_label = tk.Label(entry, text="Enter password name:")
        name_entry = tk.Entry(entry)

        name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        get_button = tk.Button(entry, text="Get Password", command=lambda: self.get_password(entry, name_entry.get()))
        get_button.grid(row=1, column=0, columnspan=2, pady=10)

    def get_password(self, entry, name):
        if not name:
            messagebox.showerror("Error", "Please enter a name.")
            return

        password, comment = self.password_manager.get_password(name)
        if password is not None:
            messagebox.showinfo("Password", f"Password for '{name}': {password}\nComment: {comment}")
        else:
            messagebox.showinfo("Password", f"No password found for '{name}'.")
        entry.destroy()

    def show_update_password_entry(self):
        entry = tk.Toplevel(self.menu)
        entry.title("Update Password")

        name_label = tk.Label(entry, text="Enter password name:")
        name_entry = tk.Entry(entry)
        new_password_label = tk.Label(entry, text="Enter new password:")
        new_password_entry = tk.Entry(entry)

        name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        new_password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        new_password_entry.grid(row=1, column=1, padx=10, pady=5)

        update_button = tk.Button(entry, text="Update Password",
                                  command=lambda: self.update_password(entry, name_entry.get(),
                                                                       new_password_entry.get()))
        update_button.grid(row=2, column=0, columnspan=2, pady=10)

    def update_password(self, entry, name, new_password):
        if not name:
            messagebox.showerror("Error", "Please enter a name.")
            return

        if self.password_manager.update_password(name, new_password):
            messagebox.showinfo("Success", f"Password for '{name}' updated successfully.")
        else:
            messagebox.showinfo("Password", f"No password found for '{name}'.")
        entry.destroy()

    def show_delete_password_entry(self):
        entry = tk.Toplevel(self.menu)
        entry.title("Delete Password")

        name_label = tk.Label(entry, text="Enter password name:")
        name_entry = tk.Entry(entry)

        name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        delete_button = tk.Button(entry, text="Delete Password",
                                  command=lambda: self.delete_password(entry, name_entry.get()))
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    def delete_password(self, entry, name):
        if not name:
            messagebox.showerror("Error", "Please enter a name.")
            return

        if self.password_manager.delete_password(name):
            messagebox.showinfo("Success", f"Password for '{name}' deleted successfully.")
        else:
            messagebox.showinfo("Password", f"No password found for '{name}'.")
        entry.destroy()

    def generate_new_passwords(self):
        self.password_manager.generate_new_passwords()

    def quit_menu(self):
        self.menu.destroy()

    def show_menu(self):
        self.menu.mainloop()

if __name__ == '__main__':
    gui = PasswordManagerGUI()
    gui.show_password_manager_menu()

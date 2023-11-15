import argparse
import string
import itertools
import time

def crack_password(password, mode, search_space, length, k=None):
    attempts = 0
    start_time = time.time()

    if mode == 1:
        for char in search_space:
            attempts += 1
            if char == password:
                break
    elif mode == 2:
        for guess in itertools.product(search_space, repeat=len(password)):
            attempts += 1
            if ''.join(guess) == password:
                break
    elif mode == 3:
        password_length = len(password)
        k = min(k, password_length)
        for k_chars in itertools.permutations(search_space, k):
            for guess in itertools.product(k_chars, repeat=password_length):
                attempts += 1
                if ''.join(guess) == password:
                    break
            else:
                continue
            break
        else:
            attempts = -1  # If the password wasn't found within the given k characters

    end_time = time.time()
    execution_time = end_time - start_time
    return attempts, execution_time

def main():
    parser = argparse.ArgumentParser(description="Password Cracker Tool")
    parser.add_argument("password", help="Password to crack")
    parser.add_argument("mode", type=int, choices=[1, 2, 3], help="Select mode (1: Known first character, 2: Standard, 3: Known k characters)")
    parser.add_argument("search_space", choices=['numbers', 'lowercase', 'uppercase', 'character', 'all'], help="Select search space (numbers, lowercase, uppercase, character, all)")
    parser.add_argument("n", type=int, help="Specify the length of password")
    parser.add_argument("k", type=string, help="Specify a part of password")

    args = parser.parse_args()

    if args.search_space == 'numbers':
        search_space = string.digits
    elif args.search_space == 'lowercase':
        search_space = string.ascii_lowercase
    elif args.search_space == 'uppercase':
        search_space = string.ascii_uppercase
    elif args.search_space == 'character':
        search_space = string.ascii_characters
    else:
        search_space = string.ascii_letters + string.digits + string.ascii_characters

    attempts, execution_time = crack_password(args.password, args.mode, search_space, args.n, args.k)

    if attempts == -1:
        print(f"Password not found within the specified {args.k} characters.")
    else:
        print(f"Password cracked: {args.password}")
        print(f"Attempts: {attempts}")
        print(f"Execution Time: {execution_time} seconds")

if __name__ == "__main__":
    main()

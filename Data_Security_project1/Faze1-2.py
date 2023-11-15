import argparse
import string

def crack_password(password, mode, search_space, length, k=None):
    attempts = 0
    
    #time required when computing 10^6 encryption per second 
    execution_time = 0
    execution_time_unit = ""

    if mode == 1:
        attempts, execution_time, execution_time_unit = mode1(length, search_space)
    elif mode == 2:
        attempts, execution_time, execution_time_unit = mode1(length-1, search_space)
    elif mode == 3 and k!=None:
        attempts, execution_time, execution_time_unit = mode1(length-(len(k)), search_space)
    else:
        attempts, execution_time, execution_time_unit = -1, 0, ""
    return attempts, execution_time , execution_time_unit


def mode1(length, search_space):
    bits = (pow(len(search_space), length)*8)
    attempts = pow(2, bits)
    #time required when computing 10^6 encryption per second 
    execution_time = (attempts/2)/pow(10,(-12))
    execution_time_unit = ""
    if bits < 40:
            execution_time *= pow(10,3)
            execution_time_unit = 'milliseconds'
    elif bits < 46:
            execution_time_unit = 'seconds'
    elif bits < 52:
            execution_time /= 60
            execution_time_unit = 'minutes'
    elif bits < 57:
            execution_time /= (60*60)
            execution_time_unit = 'hours'
    elif bits < 60:
            execution_time /= (60*60*24)
            execution_time_unit = 'days'
    elif bits < 62:
            execution_time /= (60*60*24*7)
            execution_time_unit = 'weeks'
    elif bits < 65:
            execution_time /= (60*60*24*7*4)
            execution_time_unit = 'months'
    elif bits >= 65:
            execution_time /= (60*60*24*7*4*12)
            execution_time_unit = 'years'
    return attempts, execution_time, execution_time_unit

def main():
    parser = argparse.ArgumentParser(description="Password Cracker Tool")
    parser.add_argument("password", help="Password to crack")
    parser.add_argument("mode", type=int, choices=[1, 2, 3], help="Select mode (1: Known first character, 2: Standard, 3: Known k characters)")
    parser.add_argument("search_space", choices=['numbers', 'lowercase', 'uppercase', 'character', 'all'], help="Select search space (numbers, lowercase, uppercase, character, all)")
    parser.add_argument("n", type=int, help="Specify the length of password")
    parser.add_argument("k", help="Specify a part of password")

    args = parser.parse_args()
    # password = input("Password: ")
    # n = int(input("Length of Password: "))
    # k = input("Part of Password: ")
    # mode = int(input("Mode: "))
    # search_space = string.printable

    if args.search_space == 'numbers':
        search_space = string.digits
    elif args.search_space == 'lowercase':
        search_space = string.ascii_lowercase
    elif args.search_space == 'uppercase':
        search_space = string.ascii_uppercase
    elif args.search_space == 'character':
        search_space = string.punctuation
    else:
        search_space = string.ascii_letters + string.digits + string.punctuation

    attempts, execution_time, execution_time_unit = crack_password(args.password, args.mode, search_space, args.n, args.k)

    # attempts, execution_time, execution_time_unit = crack_password(password, mode, search_space, n, k)

    if attempts == -1:
        print(f"Password not found within the specified {args.k} characters.")
    else:
        print(f"Attempts: {attempts:g}")
        print(f"Execution Time: {execution_time} {execution_time_unit}")

if __name__ == "__main__":
    main()

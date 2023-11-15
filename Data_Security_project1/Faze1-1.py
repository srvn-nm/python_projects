import argparse
import string

parser = argparse.ArgumentParser(description="Password Security Assessment Tool")
parser.add_argument("password", help="Password")

args = parser.parse_args()


def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = special_char_count = length = common = 0

#lowercase, uppercase, digits
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        else:
            special_char_count += 1
    
#dictionary check
    with open("10-million-password-list-top-1000000.txt", 'r') as file:
        content = file.read()

        if password not in content:
            common += 1
            

#length of the password
    if len(password) >= 12:
       length += 1 
       
#strength grading
    strength = 0

    if lower_alpha_count >= 1:
        strength += 1

    if upper_alpha_count >= 1:
        strength += 1

    if number_count >= 1:
        strength += 1

    if special_char_count >= 1:
        strength += 1

    if length == 1:
        strength += 1

    if common == 1:
        strength += 1
        
    return strength


grade = check_password_strength(args.password)
print("The security strength grade is " + str(grade) + " out of 7! : " + str(grade/7))
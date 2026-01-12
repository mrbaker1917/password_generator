import re
import secrets
import string


def generate_password(length=8, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    # symbols = string.punctuation
    symbols = "$@#_!&"

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ""
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r"\d"),
            (special_chars, rf"[{symbols}]"),
            (uppercase, r"[A-Z]"),
            (lowercase, r"[a-z]"),
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password

def inputter():
    print("Welcome to the Password Generator!")
    length = int(input("Please enter the length the password you would like to create: "))
    if length < 8 or length > 50:
        print("Passwords should be at least 8 characters in length and no more tha 50.")
        return
    nums = int(input("How many numbers would you like included in the password? "))
    special_chars = int(input("How many special characters would you like in the password? "))
    upper_case = int(input("How many uppercase letters would you like? "))
    lower_case = int(input("How many lowercase letters would you like? "))
    if (nums+special_chars+upper_case+lower_case) > length:
        print("Too many characters for length! Please make sure you do not request more characters than the total length.")
        return
    new_password = generate_password(length, nums, special_chars, upper_case, lower_case)
    print(f"Here is your new password: '{new_password}'")

if __name__ == "__main__":
    inputter()
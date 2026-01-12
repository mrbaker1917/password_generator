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


if __name__ == "__main__":
    print("Welcome to the password generator!")
    length = int(input("Please enter the length the password you would like to create: "))
    nums = int(input("How many numbers would you like included in the password? "))
    special_chars = int(input("How many special characters would you like in the password? "))
    upper_case = int(input("How many upper care letters would you like? "))
    lower_case = int(input("How many lower case letters would you like? "))
    new_password = generate_password(length, nums, special_chars, upper_case, lower_case)
    print("Here is your new password: ", new_password)

"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    extra_info = ""
    if SPECIAL_CHARS_REQUIRED:
        extra_info = "and special {}".format(SPECIAL_CHARACTERS)
    print("One or more uppercase, lowercase, numeric {} characters".format(extra_info))

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if int(password.count('')) > MAX_LENGTH + 1:
        print("Password too long")
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        else:
            for i in SPECIAL_CHARACTERS:
                if i == char:
                    count_special += 1

    print("Password has: {} lowercase, {} uppercase, {} numeric and {} special characters"
          .format(count_lower, count_upper, count_digit, count_special))

    if count_lower <= 0:
        return False

    if count_upper <= 0:
        return False

    if count_digit <= 0:
        return False

    if SPECIAL_CHARS_REQUIRED:
        if count_special <= 0:
            return False

    # if we get here (without returning False), then the password must be valid
    return True


main()

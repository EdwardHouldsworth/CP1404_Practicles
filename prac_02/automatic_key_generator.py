import random

NUMBERS = "0123456789"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

finished = False
key_upper = False
key_number = False
key_special = False
key_length = 6


def get_yesno_answer(question="default"):
    answer = input(question)
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False


if get_yesno_answer("Do you want Uppercase (Y/N)? "):
    key_upper = True
if get_yesno_answer("Do you want Numbers (Y/N)? "):
    key_number = True
if get_yesno_answer("Do you want Special Symbols (Y/N)? "):
    key_special = True

finished = False
while not finished:
    try:
        key_length = int(input("How long should the Password be? "))
        finished = True
    except ValueError:
        print("Password length incorrect")

setof_symbol_choices = ALPHA
if key_upper:
    setof_symbol_choices += ALPHA.upper()
if key_number:
    setof_symbol_choices += NUMBERS
if key_special:
    setof_symbol_choices += SPECIAL_CHARACTERS

generated_password = ""
for x in range(0, key_length):
    generated_password += random.choice(setof_symbol_choices)

# probably should gaurentee symbol requirements

print(generated_password)

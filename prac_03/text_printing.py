"""Edward Houldsworth"""

"""
**On paper**, write a program that asks the user for some text, with
error-checking to repeat until the text is not blank. The program should
then print every second letter in the provided text. Example: if the
user enters "Pythonista", the program should print "Ptoit".
"""


def main():
    user_text = get_text()
    skip_amount = get_skip_amount()
    print(skip_letters(user_text, skip_amount))


def skip_letters(text_str, incremental_skip):
    temp_string = ""
    for x in range(0, len(text_str), incremental_skip):
        temp_string += text_str[x]
    return temp_string


def get_skip_amount():
    skip_amount = 0
    finished = False
    while not finished:
        try:
            skip_amount = int(input("Enter the amount of characters to skip: "))
            finished = True
        except ValueError:
            print("Invalid input")
    return skip_amount


def get_text():
    user_text = input("Enter some text: ")
    while user_text == "":
        print("Invalid input")
        user_text = input("Enter some text: ")
    return user_text


main()

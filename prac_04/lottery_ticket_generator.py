"""
Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Each line should not contain any repeated number.
Make sure your numbers are unique.
Each line of numbers should be displayed in sorted (ascending) order.
"""

import random

NUMBER_SET = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
              17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
              31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]


def main():
    number_of_quickpicks = int(input("How many quickpicks? "))
    quickpicks = [[0]]
    quickpicks = generate_quickpicks(number_of_quickpicks, quickpicks)
    quickpicks.remove([0])
    display_quickpicks(quickpicks)
    print("Done")


def display_quickpicks(quickpicks):
    quickpicks.sort()
    for element in quickpicks:
        print("{:<3} {:<3} {:<3} {:<3} {:<3}"
              .format(element[0], element[1], element[2], element[3], element[4]))


def generate_quickpicks(number_of_quickpicks, quickpicks):
    for x in range(0, number_of_quickpicks):
        valid_ticket = False
        while not valid_ticket:
            ticket = generate_ticket()
            valid_ticket = check_ticket(ticket, quickpicks)
            # print(check_ticket(ticket, quickpicks))
            if valid_ticket:
                quickpicks += [ticket]
    return quickpicks


def generate_ticket():
    single_ticket = []
    for y in range(1, 7):
        single_ticket += [random.choice(NUMBER_SET)]
    single_ticket.sort()
    return single_ticket


def check_ticket(ticket, current_quickpicks):
    valid_ticket = False
    for element in current_quickpicks:
        if ticket != element:
            valid_ticket = True
    for x in ticket:
        if ticket.count(x) >= 2:
            valid_ticket = False
            break
    return valid_ticket


main()

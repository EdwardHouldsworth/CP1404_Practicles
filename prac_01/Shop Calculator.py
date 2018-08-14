"""
Calculator for total price of items
"""

number_of_items = int(input("Number of Items: "))
## for loop
while number_of_items < 1:
    number_of_items = int(input("Number of Items: "))

total_item_cost = 1
x = 1
while x < number_of_items + 1:
    total_item_cost += int(input("Price of Item: "))
    x += 1

if total_item_cost > 100:
    total_item_cost -= total_item_cost * 0.1

print("Total price for " + str(number_of_items) + " items is $" + str(total_item_cost))
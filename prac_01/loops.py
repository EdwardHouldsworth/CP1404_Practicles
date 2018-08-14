"""
Various Loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print("Done")

for i in range(0, 101, 10):
    print(i, end=' ')
print("Done")

for i in range(20, 0, -1):
    print(i, end=' ')
print("Done")

number_of_stars = int(input("How many stars do you want to print? "))
print("*" * number_of_stars)

for i in range(1,number_of_stars + 1,1):
    print("*" * i)
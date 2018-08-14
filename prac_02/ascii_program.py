# ASCII guessing program

LOWER = 33
UPPER = 127
finished = False
column_amount = 1

while not finished:
    try:
        column_amount = int(input("ASCII table columns(1-9)?: "))
        finished = True
    except ValueError:
        print("Invalid Input")

if column_amount > 9:
    column_amount = 9
elif column_amount < 1:
    column_amount = 1

column_length = (127 - 33) // column_amount
listof_columns = []

for x in range(33, 128):
    temp_str = "{:>4} <-> {:<4}".format(x, chr(x))
    listof_columns.append(temp_str)

for x in range(0, column_length):
    temp_str = ""
    for y in range(0, column_length * column_amount, column_length):
        temp_str += listof_columns[x + y]
    print(temp_str)

finished = False
while not finished:
    input_string = str(input("Enter a number (33->127) or letter: "))
    if input_string.isnumeric():
        if int(input_string) > 33 or int(input_string) < 127:
            print("The Character for {} is {}".format(input_string, chr(int(input_string))))
    elif input_string.isalpha():
        print("The ASCII code for {} is {}".format(input_string, ord(input_string)))
    elif input_string == '':
        finished = True
    else:
        print("Invalid input.")

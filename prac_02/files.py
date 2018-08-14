"""
Write a program that asks the user for their name,
 then opens a file called "name.txt" and writes that name to it.
"""

output_file = open("name.txt", 'w')
name = str(input("Enter your name: "))
# print(name, file = output_file)
output_file.write(name)

name = ""
output_file.close()

"""
Write a program that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""

input_file = open("name.txt", 'r')
name = input_file.readline()
print("Your name is {}".format(name))

input_file.close()

"""
Create a text file called "numbers.txt" 
(You can create a simple text file in PyCharm with Ctrl+N, 
choose "File" and save it in your project). Put the numbers 
17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens "numbers.txt", reads the numbers 
and adds them together then prints the result, which should be... 59.
"""

input_file = open("numbers.txt", 'r')
number_A = input_file.readline()
number_B = input_file.readline()
print(number_A + number_B)

number_total = 0
for i in input_file:
    number_total += int(i)
print(number_total)

input_file.close()

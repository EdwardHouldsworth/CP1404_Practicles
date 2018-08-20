numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[0:])
print(numbers[1:5])
print(5 in numbers)
print(1 in numbers)
print(3 in numbers)
#print(numbers + [6, 500, 3] + [7])
#numbers += [6, 500, 3]

numbers[0] = "ten"
numbers[-1] = "one"
print(numbers)
print(numbers[2:])
print(9 in numbers)
# first part
numbers = []

for i in range(50,60+1):
    numbers.append(i)

# Second Part
even_numbers = []

for index in range(0, len(numbers)):
    if numbers[index] % 2 == 0:
        even_numbers.append(str(numbers[index]) + "-" + str(index))

print(numbers)
print(even_numbers)
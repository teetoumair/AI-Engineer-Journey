#15-Copy.py


numbers_1 = [10, 20, 30]
numbers = [10, 20, 30]

print("We need to copy because if we assign numbers_1 to new_numbers, then any changes made to new_numbers will also affect numbers_1. This is because both variables will point to the same list in memory.")


new_numbers = numbers_1
numbers_1.append(40)


print("Here is the copy version of the list:")

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers_1)
print(new_numbers)
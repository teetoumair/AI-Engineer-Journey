numbers = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

unique_number = {number for number in numbers}

print(unique_number)

numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = {value: value**2 for value in numbers_2 if value % 2 == 0}

print(even_numbers)
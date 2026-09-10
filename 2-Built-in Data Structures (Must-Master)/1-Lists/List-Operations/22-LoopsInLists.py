#22-LoopsInLists.py

numbers = [3, 8, 12, 5, 20, 7, 15]

for number in numbers:
    if number % 2 == 0:
        print(number)

new_list = []

for number in numbers:
    if number % 2 == 0:
        new_list.append(number**2)

print(new_list)

numbers = [10, 20, 5, 15, 30]

total = 0

for value in numbers:
    total = total+value

print(total)

numbers = [10, 15, 20, 7, 30, 11, 40]

total = 0

for val in numbers:
    if val % 2 == 0:
        total = total + val

print(total)

numbers = [4, 9, 16, 3, 25, 8, 12]

new_list.clear()

for number in numbers:
    if number > 10:
        new_list.append(number**2)

print(new_list)

numbers = [5, 12, 7, 20, 3, 18, 10, 25]

new_list = []

for number in numbers:
    if number > 10:
        if number % 2 == 0:
            new_list.append(number)

print(new_list)
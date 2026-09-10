#23-FunctionInLists.py

def get_even_numbers(numbers):

    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)

    return new_list

def add_number(numbers):
    numbers.append(100)

numbers = [10, 15, 22, 7, 30, 9]

result = get_even_numbers(numbers)
add_number(numbers)

print(numbers)
print(result)

def remove_duplicates(numbers):
    unique_set = set(numbers)
    return list(unique_set)
    
        

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_list = list(remove_duplicates(numbers))

print(unique_list)
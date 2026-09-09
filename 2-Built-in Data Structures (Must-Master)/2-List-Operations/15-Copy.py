#15-Copy.py

numbers = [10, 20, 30]

# Reference — same list
new_numbers = numbers

new_numbers.append(40)

print(numbers)
print(new_numbers)

print("")
# Copy — separate list
copied_numbers = numbers.copy()

copied_numbers.append(50)

print(numbers)
print(copied_numbers)

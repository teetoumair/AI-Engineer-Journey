#3-Appending-vs-Extending

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)

#wrong way to add multiple elements as append will consider it as a single element
numbers.append([50, 60])
print(numbers)

#right way to add multiple elements
numbers.extend([50, 60])
print(numbers)
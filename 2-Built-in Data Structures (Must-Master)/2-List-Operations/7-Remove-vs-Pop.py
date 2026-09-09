#7-Remove-vs-Pop.py

numbers = [10, 20, 30, 40]

print("Numbers before remove operation")
print(numbers)

print("Numbers after remove operation")
numbers.remove(30)
print(numbers)

print("Numbers before pop operation")
numbers = [10, 20, 30, 40]
print(numbers)

#in case no specific index is provided, pop() removes the last element from the list.

print("Numbers after pop operation")
numbers.pop(1)
print(numbers)

print("Pop operation basically removes an element based in the index, while remove operation removes an element based on the value, as u can see in the implementation.")
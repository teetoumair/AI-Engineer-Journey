#2-Remove-vs-Discard.py

numbers = {10, 20, 30, 40}

#Gives error when value not found
numbers.remove(20)

#not Gives Error when value not found
numbers.discard(50)

print(numbers)
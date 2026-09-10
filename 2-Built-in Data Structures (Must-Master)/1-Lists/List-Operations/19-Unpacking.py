#19-Unpacking.py

#normal Unpacking

student = ["Umair", 22, "AI Engineer"]

name, age, career = student

print("My name is " + name)
print("I am " + str(age) + " years old.")
print("My career is " + career)

#Unpacking with * operator

numbers = [1, 2, 3, 4, 5, 6, 7]

first, second, *bheech_walay, secondLast, Last = numbers

print("First Number: " + str(first))
print("Second Number: " + str(second))
print("Bheech walay Numbers: " + str(bheech_walay))
print("Second Last Number: " + str(secondLast))
print("Last Number: " + str(Last))
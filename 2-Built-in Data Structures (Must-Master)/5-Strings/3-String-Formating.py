#3-String-Formating.py

student = {"name": "Ali", "age": 25, "cgpa": 3.87, "fees": 85000}

"""
f-string se report line banao: "Ali is 25 years old with 3.87 CGPA" — dict ke keys se values nikaal kar
fees ko comma wale format mein print karo (85,000)
cgpa ko 2 decimal tak print karo (3.87 likha tha, ek aur pakka karo kuch)
Ek calculated expression f-string ke andar: cgpa ka square nikalo
"""

print(f"{student['name']} is {student['age']} years old with {student['cgpa']}")

print(f"{student['fees']:,}")

print(f"{student['cgpa']:.2f}")
print(f"square of the cgpa is {(student['cgpa'])**2}")
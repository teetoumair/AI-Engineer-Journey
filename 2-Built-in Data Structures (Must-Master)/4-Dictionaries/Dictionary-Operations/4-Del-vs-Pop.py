#4-Del-vs-Pop.py

user_details = {
    "name" : "Ali",
    "position" : "AI Engineer",
    "salary" : 150000,
    "experience": 2
}

print(user_details)
del user_details["experience"]
print(user_details)

#del user_details["naam"] will give an error.

print(user_details.pop("naam", "not Found")) #will not give an error

removed = user_details.pop("salary")
print("Salary is removed which had value", removed)

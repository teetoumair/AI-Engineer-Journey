#1-Dictionaries.py

user_details = {
    "name" : "Ali",
    "position" : "AI Engineer",
    "salary" : 150000
}


print(user_details["name"])
print(user_details["position"])

user_details["salary"] = 180000
user_details["experience"] = 2

print(user_details)

del user_details["experience"]

print(user_details)
#2-Update-and-Setdefault.py

a = {"apple": 1, "banana": 2}
b = {"banana": 5, "mango": 3}

user = {"name": "Ali"}

a.update(b)

print(a)

print(user.setdefault("name", "unknown"))
print(user.setdefault("age", 25))
print(user.setdefault("age", 30))
print(user["age"])
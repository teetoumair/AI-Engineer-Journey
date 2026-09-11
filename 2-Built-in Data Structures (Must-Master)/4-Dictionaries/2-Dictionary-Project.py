#2-Dictionary-Project.py

grades = {
    "Ali": 85, "Sara": 92, "Zain": 68,
    "Umaima": 74, "Hamza": 58, "Rabia": 90
}

"""
Har student ka naam aur grade print karo
Un students ke names print karo jinka grade > 80
Fail students (grade < 60) remove karo (mutability demo — remove karo aur len() ab kya hai)
Ek dict chahiye jisme passing students hon — failing wale pure program mein na aayein, ya pop() use karke waghera

"""

for i in grades:
    print(i+":", grades[i])

print("\nFollowing are the students who got more than 80:")
for i in grades:
    if grades[i]> 80:
        print(i)

for i in list(grades):   # list(grades) = keys ki copy — original safe
    if grades[i] < 60:
        name = i
        marks = grades.pop(i)
        print("student", name, "has been removed on being failed cz he had", marks, "marks")

print(len(grades))

passing_students = {}
for name, marks in grades.items():
    if marks >= 60:
        passing_students[name] = marks

print(passing_students)

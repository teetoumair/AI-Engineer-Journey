#6-Iteration.py

meetup_members = {
    "Ali": 25,
    "Sara": 30,
    "Zain": 22,
    "Umaima": 27
}

for i in meetup_members:
    print(i)

for i in meetup_members:
    print(meetup_members[i])

for i in meetup_members:
    print(str(i)+":", meetup_members[i])

for i in meetup_members:
    age = meetup_members[i]
    if age > 24:
        print(i)
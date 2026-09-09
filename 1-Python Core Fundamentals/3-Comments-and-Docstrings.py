#Code is taking Inputs here by using input function and then it is checking the experience of the user and printing the level of the user based on the experience.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))

def get_level(experience):

    """Determine the user's professional level from experience."""
    if experience < 1:
        return "Fresher"
    elif experience < 2:
        return "Junior"
    else:
        return "Senior"

#Code is Printing the details of the user including name, age, experience and level based on the experience.
print("Name:", name)
print("Age:", age)
print("Experience:", experience)
print("Level:", get_level(experience))
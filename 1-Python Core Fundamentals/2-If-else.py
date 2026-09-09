Experience=float(input("Enter your years of experience: "))

if Experience < 1:
    print("Fresher")
elif Experience < 2:
    print("Junior")
else:
    print("Senior")
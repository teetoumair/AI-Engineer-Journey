name = "Ali"
age = 25
current_salary = 50000

if age >= 18:
 print(name, "is eligible")
else:
 print(name, "is not eligible")


def calculate_salary(current_salary, DesiredSalary):
    salary_difference = DesiredSalary - current_salary
    required_increase = (salary_difference / current_salary) * 100
    return salary_difference, required_increase


result = calculate_salary(50000, 60000)
print(result)
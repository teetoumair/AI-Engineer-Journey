def calculate_salary_increase(current_salary, desired_salary):
    salary_difference = desired_salary - current_salary
    required_increase = (salary_difference / current_salary) * 100
    return salary_difference, required_increase

result = calculate_salary_increase(5000, 20000)

print(result[1])
print(result[0])
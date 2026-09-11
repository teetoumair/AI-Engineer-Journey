#7-Nested-Dictionaries.py

company = {
    "Ali":   {"role": "AI Engineer", "salary": 150000},
    "Sara":  {"role": "ML Engineer",  "salary": 180000},
    "Zain":  {"role": "Data Analyst", "salary": 90000}
}

"""company["Ali"] print karo — kya milega?
Sirf Ali ka salary print karo (2-index access)
Har member ka naam aur uska salary "ke: salary" form mein print karo (nested loop)
Total salary total karo (sab salaries jama karo) aur print karo"""

print(company["Ali"])
print("Ali's Salary is:", company["Ali"]["salary"])
for i in company:
    print(i + ":", company[i]["salary"])


total = 0
for i in company:
    total += company[i]["salary"]

print("Total of salaries:", total)
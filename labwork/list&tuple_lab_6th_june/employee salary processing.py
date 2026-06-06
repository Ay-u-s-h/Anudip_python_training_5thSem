# Problem 4: Employee Salary Processing

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# 1. Display employees earning above ₹50,000
print("Employees earning above ₹50,000:")
for name, salary in employees:
    if salary > 50000:
        print(name, "-", salary)

# 2. Find the highest-paid employee
highest_paid = max(employees, key=lambda x: x[1])
print("\nHighest paid employee:", highest_paid[0], "-", highest_paid[1])

# 3. Calculate total salary expenditure
total_salary = sum([salary for _, salary in employees])
print("\nTotal salary expenditure:", total_salary)

# 4. Count employees earning below ₹40,000
count_below_40000 = sum(1 for _, salary in employees if salary < 40000)
print("\nEmployees earning below ₹40,000:", count_below_40000)

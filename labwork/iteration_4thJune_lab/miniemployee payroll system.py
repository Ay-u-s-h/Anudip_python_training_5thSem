# Program: Employee Payroll System
# Task: Calculate Gross, Net Salary, and Grade.

# Input employee details
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculate components
hra = 0.20 * basic_salary
da = 0.10 * basic_salary
pf = 0.12 * basic_salary

gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Determine grade
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Display results
print(f"\nEmployee Name: {name}")
print(f"Gross Salary: ₹{gross_salary}")
print(f"Net Salary: ₹{net_salary}")
print(f"Grade: {grade}")

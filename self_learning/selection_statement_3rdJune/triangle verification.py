# Program: Triangle Verification
# Task: Accept three sides and check if they form a valid triangle.
# Rule: For a valid triangle, sum of any two sides must be greater than the third side.

# Input three sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check triangle validity using triangle inequality theorem
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a valid Triangle.")
else:
    print("The sides do NOT form a Triangle.")

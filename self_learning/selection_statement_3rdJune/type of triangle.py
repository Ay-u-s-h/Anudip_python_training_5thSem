# Program: Type of Triangle
# Task: Accept three sides, check validity, then determine type.
# Types: Equilateral, Isosceles, Scalene

# Input three sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# First check if valid triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a valid Triangle.")
    
    # Check type of triangle
    if a == b == c:
        print("It is an Equilateral Triangle.")
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle.")
    else:
        print("It is a Scalene Triangle.")
else:
    print("The sides do NOT form a Triangle.")

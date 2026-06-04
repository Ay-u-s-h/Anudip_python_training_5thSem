# Program: Strong Number Verification
# Task: Check if sum of factorials of digits = number

import math

num = int(input("Enter a number: "))
sum_of_factorials = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_factorials += math.factorial(digit)
    temp //= 10

if sum_of_factorials == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a Strong Number")

# Program: Armstrong Number Checker
# Task: Check if a number is Armstrong (sum of cubes of digits = number)

num = int(input("Enter a number: "))
sum_of_cubes = 0

# Copy of number for processing
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if sum_of_cubes == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")

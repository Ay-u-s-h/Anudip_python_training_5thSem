# Program: Secret Code Validator
# Task: Valid if 6 digits and sum(first 3) == sum(last 3).

code = input("Enter 6-digit code: ")

# Check length and sum condition
if len(code) == 6 and sum(map(int, code[:3])) == sum(map(int, code[3:])):
    print("Valid Code")
else:
    print("Invalid Code")

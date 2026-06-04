# Program: Consecutive Digit Number
# Task: Check if every digit is exactly 1 greater than the previous digit.

num = input("Enter a number: ")
is_consecutive = True

for i in range(len(num) - 1):
    if int(num[i+1]) - int(num[i]) != 1:
        is_consecutive = False
        break

if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")


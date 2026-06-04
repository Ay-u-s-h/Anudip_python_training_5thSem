# Program: Mountain Number
# Task: Digits first increase then decrease.

num = input("Enter a number: ")
peak_found = False
is_mountain = True

for i in range(1, len(num)):
    if not peak_found:
        if num[i] < num[i-1]:
            peak_found = True
    else:
        if num[i] > num[i-1]:
            is_mountain = False
            break

if peak_found and is_mountain:
    print("Mountain Number")
else:
    print("Not a Mountain Number")

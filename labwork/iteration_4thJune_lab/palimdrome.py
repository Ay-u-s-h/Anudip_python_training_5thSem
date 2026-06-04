# Program: Palindrome and Reverse Number Checker
# Task: Accept a number, display reverse, check palindrome.

num = int(input("Enter a number: "))
reverse = int(str(num)[::-1])  # Reverse using string slicing

print(f"Reverse: {reverse}")

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome")

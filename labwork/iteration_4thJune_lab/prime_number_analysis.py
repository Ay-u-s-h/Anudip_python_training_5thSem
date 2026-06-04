# Program: Prime Number Analyser
# Task: Accept a number, check if prime. If not, display its factors.

num = int(input("Enter a number: "))

# Flag to check prime status
is_prime = True

# Collect factors
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
        # If divisible by something other than 1 and itself, not prime
        if i != 1 and i != num:
            is_prime = False

# Display results
print("Factors:", *factors)
if is_prime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")


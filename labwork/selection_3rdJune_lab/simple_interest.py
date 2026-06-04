# Program: Simple Interest Calculator
# Formula: SI = (P * R * T) / 100
# P = Principal, R = Rate of Interest, T = Time (in years)

# Take inputs from the user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

# Validate inputs (they must be positive)
if principal <= 0 or rate <= 0 or time <= 0:
    print("Invalid input! All values must be positive.")
else:
    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100
    
    # Display the result
    print(f"Simple Interest = {simple_interest}")


# Program: Electricity Bill Simulator
# Task: Calculate bill using slabs and add surcharge if bill > 5000.

units = int(input("Enter units consumed: "))

# Calculate bill based on slabs
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Add surcharge if bill exceeds 5000
if bill > 5000:
    bill += bill * 0.10

# Display result
print(f"Final Payable Amount: ₹{bill}")

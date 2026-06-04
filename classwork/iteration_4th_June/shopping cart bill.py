# Program: Shopping Cart Bill
# Problem: A customer adds item prices one by one.
# Task: Keep accepting item prices, add them to the total bill,
#       and stop when the user enters 0.

# Initialize total bill amount
total_bill = 0

# Infinite loop to keep asking for item prices
while True:
    # Ask the user to enter the price of an item
    price = int(input("Enter Item Price: "))
    
    # If the user enters 0, stop the loop
    if price == 0:
        break
    
    # Add the entered price to the total bill
    total_bill += price

# After the loop ends, display the total bill amount
print(f"\nTotal Bill Amount: ₹{total_bill}")

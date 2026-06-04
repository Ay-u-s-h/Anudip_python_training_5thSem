# Program: PIN Verification
# Problem: An ATM requires the user to enter the correct PIN (1234).
# Task: Keep asking for the PIN until the correct one is entered.

# Define the valid PIN
valid_pin = "1234"

# Initialize a variable to store user input
entered_pin = ""

# Use a loop to keep asking until the correct PIN is entered
while entered_pin != valid_pin:
    # Ask the user to enter a PIN
    entered_pin = input("Enter PIN: ")
    
    # Check if the entered PIN is correct
    if entered_pin == valid_pin:
        print("Access Granted.")
    else:
        print("Incorrect PIN. Try Again.")

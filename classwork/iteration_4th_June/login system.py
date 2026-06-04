# Program: Login System
# Problem: A website allows users to log in using a password.
# Task: Keep asking for the password until the correct one ("admin123") is entered.

# Define the correct password
correct_password = "admin123"

# Initialize a variable to store user input
entered_password = ""

# Use a loop to keep asking until the correct password is entered
while entered_password != correct_password:
    # Ask the user to enter a password
    entered_password = input("Enter Password: ")
    
    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Login Successful.")
    else:
        print("Invalid Password.")

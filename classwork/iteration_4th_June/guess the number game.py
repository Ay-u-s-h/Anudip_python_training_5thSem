# Program: Guess the Number Game
# Problem: The secret number is 7. The player must keep guessing until correct.
# Task: Ask the user to guess repeatedly and display success when correct.

# Define the secret number
secret_number = 7

# Initialize a variable to store the user's guess
guess = None

# Use a loop to keep asking until the correct number is guessed
while guess != secret_number:
    # Ask the user to enter a guess
    guess = int(input("Guess the Number: "))
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Wrong Guess. Try Again.")

# Program: Number Guessing Game
# Task: Guess secret number between 1 and 50, show attempts.

secret_number = 25  # You can change this
attempts = 0
guess = None

while guess != secret_number:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1
    
    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("Correct Guess!")
        print(f"Total Attempts: {attempts}")

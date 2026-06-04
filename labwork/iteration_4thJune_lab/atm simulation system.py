# Program: ATM Simulation System
# Task: Menu-driven ATM with balance, deposit, withdraw, exit.

balance = 10000

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Current Balance: ₹{balance}")
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print(f"₹{amount} deposited. New Balance: ₹{balance}")
    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn. New Balance: ₹{balance}")
    elif choice == 4:
        print("Thank you for using ATM. Goodbye!")
        break
    else:
        print("Invalid Choice. Try Again.")

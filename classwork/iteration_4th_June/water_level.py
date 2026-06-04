# Program: Water Tank Filling
# Problem: A water tank is filled at a constant rate of 10 liters per minute.
# Task: Display the water level after each minute until the tank reaches 100 liters.

# Define the filling rate (liters per minute)
filling_rate = 10

# Define the maximum capacity of the tank (liters)
max_capacity = 100

# Start with an empty tank
current_level = 0

# Use a loop to simulate filling the tank
while current_level < max_capacity:
    # Increase the water level by the filling rate
    current_level += filling_rate
    
    # Display the current water level
    print(f"Water Level: {current_level} liters")

# Once the loop ends, the tank is full
print("Tank is full.")

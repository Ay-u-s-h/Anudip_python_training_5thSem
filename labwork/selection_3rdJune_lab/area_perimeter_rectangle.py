# Program: Rectangle Area and Perimeter
# Area = length * width
# Perimeter = 2 * (length + width)

# Take inputs from the user
length = float(input("Enter Length of Rectangle: "))
width = float(input("Enter Width of Rectangle: "))

# Validate inputs (they must be positive)
if length <= 0 or width <= 0:
    print("Invalid input! Length and Width must be positive.")
else:
    # Calculate area
    area = length * width
    
    # Calculate perimeter
    perimeter = 2 * (length + width)
    
    # Display results
    print(f"Area of Rectangle = {area}")
    print(f"Perimeter of Rectangle = {perimeter}")


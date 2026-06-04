# Program: Number Pyramid
# Task: Print pyramid and reverse pyramid based on rows.

rows = int(input("Enter number of rows: "))

# Normal pyramid
print("\nNormal Pyramid:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Reverse pyramid
print("\nReverse Pyramid:")
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

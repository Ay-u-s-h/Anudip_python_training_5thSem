#attendance tracker 
present = 0
absent = 0
n = int(input("enter total number of students:"))
for i in range(1, n + 1):
    status = input(f"Student {i} attendance (P/A): ").upper()
    if status == 'P':
        present += 1
    elif status == 'A':
        absent += 1
    else:
        print("Invalid input!")

    print("")
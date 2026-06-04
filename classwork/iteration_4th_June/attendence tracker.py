# Program: Attendance Tracker
# Problem: A teacher records attendance for a class of 30 students.
# Task: Input whether each student is Present or Absent, then display totals.

# Define the total number of students in the class
class_strength = 30

# Initialize counters for present and absent students
present_count = 0
absent_count = 0

# Loop through each student one by one
for student in range(1, class_strength + 1):
    # Ask for attendance input (Present/Absent)
    attendance = input(f"Student {student} Attendance (Present/Absent): ").strip().lower()
    
    # Check the input and update counters
    if attendance == "present":
        present_count += 1
    elif attendance == "absent":
        absent_count += 1
    else:
        # Handle invalid input
        print("Invalid input! Please enter 'Present' or 'Absent'.")
        # Repeat the same student until valid input is given
        student -= 1

# After all students are processed, display the totals
print(f"\nNo. of Students Present : {present_count}")
print(f"No. of Students Absent  : {absent_count}")

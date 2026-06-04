# Program: Attendance Counter
# Problem: A teacher records attendance as students enter the classroom.
# Task: Count the number of students entering until all 30 are present.

# Define the total number of students in the class
class_strength = 30

# Use a loop to simulate students entering one by one
for attendance_count in range(1, class_strength + 1):
    # Print message when a student enters
    print("Student Entered")
    
    # Display the current attendance count
    print(f"Attendance Count: {attendance_count}\n")

# After the loop ends, all students are present
print("All students are present.")

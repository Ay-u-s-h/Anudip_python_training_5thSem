# Program: Student Result Management System
# Task: Accept marks of 5 subjects, calculate total, percentage, grade, and failed subjects.

marks = []
failed_subjects = 0

# Input marks for 5 subjects
for i in range(1, 6):
    mark = int(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)
    if mark < 40:  # Fail condition
        failed_subjects += 1

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Display results
print(f"Total Marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
print(f"Subjects Failed: {failed_subjects}")

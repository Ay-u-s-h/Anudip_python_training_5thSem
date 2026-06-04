# Program: Longest Increasing Sequence
# Task: Find length of longest continuous increasing sequence.

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
longest = 1
current = 1

# Compare each number with the previous one
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        current += 1
        longest = max(longest, current)
    else:
        current = 1

# Display result
print(f"Longest Sequence Length = {longest}")

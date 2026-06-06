# Problem 2: Cricket Tournament Scorecard

scores = [45, 78, 12, 100, 67, 8, 90, 55]

# 1. Count half-centuries (50–99) and centuries (100+)
half_centuries = sum(1 for s in scores if 50 <= s < 100)
centuries = sum(1 for s in scores if s >= 100)
print("Half-centuries:", half_centuries)
print("Centuries:", centuries)

# 2. Find the highest score
print("Highest score:", max(scores))

# 3. Display all scores below 20
print("Scores below 20:", [s for s in scores if s < 20])

# 4. Calculate average score
average = sum(scores) / len(scores)
print("Average score:", average)

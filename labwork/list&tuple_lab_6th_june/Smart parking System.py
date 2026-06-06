# Problem 3: Smart Parking System

slots = [1, 0, 1, 1, 0, 0, 1, 0]  # 1 = Occupied, 0 = Available

# 1. Count occupied and available slots
occupied = slots.count(1)
available = slots.count(0)
print("Occupied slots:", occupied)
print("Available slots:", available)

# 2. Find the first available slot (index + 1 for human-readable slot number)
first_available = slots.index(0) + 1
print("First available slot:", first_available)

# 3. Display all available slot numbers
available_slots = [i+1 for i, s in enumerate(slots) if s == 0]
print("Available slot numbers:", available_slots)

# 4. Check whether parking occupancy exceeds 75%
occupancy_percentage = (occupied / len(slots)) * 100
print("Occupancy percentage:", occupancy_percentage, "%")
if occupancy_percentage > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy is within limit")

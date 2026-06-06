
# Problem 1: E-Commerce Order Analysis

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# 1. Display all products costing more than ₹1000
print("Products costing more than ₹1000:")
for product, price in orders:
    if price > 1000:
        print(product, "-", price)

# 2. Find the most expensive product
most_expensive = max(orders, key=lambda x: x[1])
print("\nMost expensive product:", most_expensive[0], "-", most_expensive[1])

# 3. Calculate total order value
total_value = sum([price for _, price in orders])
print("\nTotal order value:", total_value)

# 4. Count products costing below ₹1000
count_below_1000 = sum(1 for _, price in orders if price < 1000)
print("\nProducts below ₹1000:", count_below_1000)

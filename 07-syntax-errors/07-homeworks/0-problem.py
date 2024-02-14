# Fix the mistakes in the following snippet:
items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0

for item in items.keys():
    qty = int(input(f"How many {item}s, have you sold? "))
    income = income + qty * items[item]

print(f"\nThe income today was £{income:0.2f}")

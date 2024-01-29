# Take input from the user
number = int(input("Enter an integer: "))

# Print the multiplication table using a for loop
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

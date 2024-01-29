# Take input from the user
n = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(1, n + 1):
    # Inner loop for columns
    for j in range(1, i + 1):
        print(j, end=" ")  # Print the current column value followed by a space
    print()  # Move to the next line after each row

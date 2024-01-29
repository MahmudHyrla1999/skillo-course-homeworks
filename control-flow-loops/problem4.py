import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize a variable to store the user's guess
user_guess = None

# Start the guessing game loop
while user_guess != secret_number:
    # Ask the user to guess the number
    user_guess = int(input("Guess the number between 1 and 100: "))

    # Check if the guess is too high, too low, or correct
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number}!")

# End of the game

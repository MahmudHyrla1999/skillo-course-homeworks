import random


def generate_problem():
    """Generate a new random arithmetic problem for the user to solve."""
    # Choose two random numbers between 1 and 20
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    # Choose a random operator (+, -, *)
    operator = random.choice(['+', '-', '*'])
    # Generate the problem string
    problem = f"What is {num1} {operator} {num2}? "
    # Calculate the correct answer
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def play_arithmetic_game():
    """Play the arithmetic guessing game."""
    while True:
        # Generate a new problem
        problem, correct_answer = generate_problem()

        # Ask the user to solve the problem
        user_answer = int(input(problem))

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! Well done.")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing. Goodbye!")
            break


# Call the function to start the game
play_arithmetic_game()

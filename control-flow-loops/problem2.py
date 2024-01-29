# Define a function to check if the user's answer is correct
def is_correct(answer):
    try:
        # Evaluate the user's answer as a Python expression
        result = eval(answer)
        # Check if the result is correct
        return result == 22  # 5 + 17 = 22
    except:
        # If there's an error evaluating the answer, it's incorrect
        return False

# Prompt the user to solve the problem
print("How much does 5 + 17 equal to?")
# Use a loop to continue prompting the user until they provide the correct answer
while True:
    # Get the user's answer from the console
    user_answer = input("Answer: ")
    # Check if the user's answer is correct
    if is_correct(user_answer):
        # If the answer is correct, break out of the loop
        print("Correct! 5 + 17 = 22")
        break
    else:
        # If the answer is incorrect, prompt the user to try again
        print("Incorrect! Please try again.")





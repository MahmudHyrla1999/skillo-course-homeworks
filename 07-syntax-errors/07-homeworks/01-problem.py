# Rewrite the following function so it is exception safe
# def get_integer_input():
#  num = int(input("Enter an integer: "))
#   return num


# number = get_integer_input()
# print("You entered:", number)


def get_integer_input():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")


number = get_integer_input()
print("You entered:", number)

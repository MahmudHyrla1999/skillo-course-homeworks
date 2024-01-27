number_of_friends = input("How many friends do you have?")


for i in range(1, int(number_of_friends) + 1):
    ending = "th"

    if i == 1:
        ending = "st"
    elif i == 2:
        ending = "nd"
    elif i == 3:
        ending = "rd"

    input(f"What's your {i}{ending}. friend's name?")


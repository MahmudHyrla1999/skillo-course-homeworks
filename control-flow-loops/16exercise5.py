list_one = range(1, 15)


for number in list_one:
    for numberTwo in list_one:
        result = number * numberTwo
        print(f"{number} * {numberTwo} = {result}")
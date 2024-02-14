try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)


except:
    print("An unexpected error occurred")

finally:
    print("Guaranteed to be executed")

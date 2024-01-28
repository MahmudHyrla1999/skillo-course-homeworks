for i in range(1, 6):
    if i == 3:
        print("Encountered 3, breaking the loop")
        break
    elif i == 2:
        print("Encountered 2, skipping this iteration")
        continue
    else:
        print("iteration:", i)
print("Loop finished")


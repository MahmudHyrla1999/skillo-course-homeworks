num = int(input())

bonus_point = 0.0

if num <= 100:
    bonus_point = 5
elif 100 > num < 1000:
    bonus_point = num * 0.2
else:
    bonus_point = num * 0.1

if num % 2 == 0:
    bonus_point = bonus_point + 1
if num % 10 == 5:
    bonus_point = bonus_point + 2

print(bonus_point)
print(num+bonus_point)







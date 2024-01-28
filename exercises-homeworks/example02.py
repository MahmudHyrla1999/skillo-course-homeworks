age = float(input())
gender = str(input())

if gender == 'f':
    if age < 16:
        print('Miss')
    else:
        print('Ms.')
elif gender == 'M':
    if age >= 16:
        print('Mister')
    else:
        print('Master')


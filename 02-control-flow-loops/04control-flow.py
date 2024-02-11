username = 'asdf'
password = ('admin')

if username == 'admin':
    if password == 'password':
        print ('Login successful! Welcome admin.')
    elif password =='123456':
        print('Weak password.Please reset your password')
    else:
        print('Incorrect password.Please try again')
else:
    if username == 'quest':
        if password == 'quest':
            print('Login successful!.Welcome,quest.')
        else:
            print ('Incorrect password.Please try again!')
    else:
        print('Unknown user.Please try again later!')

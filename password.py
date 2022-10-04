pword ='gautam1234'
for x in range(4):
    pword2 = input(' enter your password to know e-mail id')
    if pword2 == pword:
        print('correct password and ')
        y = input('enter yes or no ')
        if y == 'yes':
            print('here is your e.mail id gautamhit***@gmail.com ')
        else:
            pass
        break
    else:
        print('wrong password')
input('hit enter to go back')

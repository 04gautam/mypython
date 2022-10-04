
try:
    print('enter your 5 subjects numbers:')
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print('your numbers are\n{}\n{}\n{}\n{}\n{}'.format(a, b, c, d, e))
    add = a + b + c + d + e
    print('your total number are ', add,'/500')

    per = add/5
    print('your percentage is ', per)

    # if per>90 exilent
    if per >= 90:
        print('grade A+\n[GREAT]')
    elif per >= 80:
        print('grade A\n[EXILENT]')
    elif per >= 70:
        print('grade B\n[VERY GOOD]')
    elif per >= 50:
        print('grade C\n[GOOD]')
    elif per >= 33:
        print('grade D\n**[POOR]**')
    else:
        print('we are sorry your are \n:(  FAIL')
except:
    print("invalid input")

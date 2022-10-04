# 2
# +
# 3
# = 5
# +
# 6
# = 11

a = int(input())
x = input()
if x == '+':
    b = int(input())
    calc = a + b
    print(calc)

    for i in range(5):
        x = input()
        if x == '+':
            b = int(input())
            calc = calc + b
            print(calc)

while True:    a = int(input())    b = str(input())    if b == '+' or b == '-' or b == '*' or b == '/' or b == '%':        c = int(input())        if b == '+':            d = a + c            print(d)        elif b == '-':            d = a - c            print(d)        elif b == '*':            d = a * c            print(d)        elif b == '/':            if c != 0:                d = a // c                print(d)        elif b == '%':            if c != 0:                d = a % c                print(d)    else:        if str(b) == '!':            if a > 0:                d = 1                for i in range(1, a + 1):                    d = d * i                print(d)            if a == 0:                print('1')    if b == 'x':        breakprint(a)
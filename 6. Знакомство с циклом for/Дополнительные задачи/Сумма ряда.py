n = int(input())e = 1summa = 0for i in range(n):    if e == 1:        b = int(input())        summa += b        e = 2    elif e == 2:        b = int(input())        summa -= b        e = 1print(summa)
a = input()len_a = len(a)real = 'abcdefghijklmnopqrstuvwxyz1234567890_'reall = set(real)flag = 'OK'dich = ''for i in range(1, len_a + 1):    ii = i - 1    if a[ii] in set(real):        continue    else:        dich = a[ii]        print('Неверный символ:', dich)        flag = 1        breakif flag == 'OK':    print(flag)
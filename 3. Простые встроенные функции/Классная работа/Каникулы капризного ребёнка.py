c1 = input()c2 = input()if c1 == c2:    print('НЕТ')else:    if c1 == 'Пенза' and c2 == 'Тула':        print('НЕТ')    else:        if c1 == 'Тула' and c2 == 'Пенза':            print('НЕТ')        else:            if c1 == 'Тула' or c2 == 'Пенза':                print('ДА')            else:                print('НЕТ')
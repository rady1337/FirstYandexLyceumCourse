terpenie = int(input())true = 0oshibok = 0e = 0while terpenie != oshibok:    a = input()    if a == 'раз':        true += 1        a = input()        if a == 'два':            true += 1            a = input()            if a == 'три':                true += 1                a = input()                if a == 'четыре':                    true += 1                else:                    print('Правильных отсчётов было',                          str(true) + ', но теперь вы ошиблись.')                    oshibok += 1                    true = 0            else:                print('Правильных отсчётов было',                      str(true) + ', но теперь вы ошиблись.')                oshibok += 1                true = 0        else:            print('Правильных отсчётов было',                  str(true) + ', но теперь вы ошиблись.')            oshibok += 1            true = 0    else:        print('Правильных отсчётов было', str(            true) + ', но теперь вы ошиблись.')        oshibok += 1        true = 0print('На сегодня хватит.')
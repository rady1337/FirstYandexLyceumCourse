kucha1 = int(input())kucha2 = int(input())while True:    nomerkuchi = int(input())    if nomerkuchi == 1:        kamni = int(input())        kucha1 = kucha1 - kamni        print(kucha1, kucha2)    elif nomerkuchi == 2:        kamni = int(input())        kucha2 = kucha2 - kamni        print(kucha1, kucha2)    if kucha1 == 0 and kucha2 == 0:        break
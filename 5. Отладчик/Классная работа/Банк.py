print('Добро пожаловать в интернет-банк!')print('У нас фантастические процентные ставки!')print('Для вкладов до 10 тысяч ₽ включительно прибыль составит 10%,')print('для вкладов на сумму до 100 тысяч включительно - 20%,')print('для более 100 тысяч - 30%!')print('На какую сумму желаете сделать вклад?')money = float(input())if money <= 10000:    money *= 1.1elif money <= 100000:    money *= 1.2elif money >= 100000:    money *= 1.3print('Вы получаете', money, '₽, поздравляем!')
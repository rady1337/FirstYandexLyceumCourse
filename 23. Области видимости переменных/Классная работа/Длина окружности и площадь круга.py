def circle_length(radius):    leng = 2 * 3.14159 * radius    return leng        def circle_area(radius):    ar = 3.14159 * (radius ** 2)        return ardef main():    global a    a = input()    if '.' in a:        a = float(a)    else:        a = int(a)    print(circle_length(a), end=' ')    print(circle_area(a))
def average(values):    a = 0    if len(values) == 0:        return 0    else:        for t in values:            a += t        b = a / len(values)        if a % len(values) == 0:            b = int(b)        return b
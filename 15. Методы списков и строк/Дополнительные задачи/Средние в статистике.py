a = input().split(' ')b = 0c = []for i in range(len(a)):    c.append(float(a[i]))for i in range(len(c)):    b += float(c[i])print(b / len(c), end=' ')c.sort()if len(c) % 2 != 0:    e = len(c) // 2    print(float(c[e]))else:    e = len(c) // 2    e1 = len(c) // 2 + 1    n = (c[e - 1] + c[e1 - 1]) / 2    print(float(n))
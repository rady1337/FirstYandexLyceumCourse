n = int(input())a = []for i in range(n):    a.append(input())p = int(input())q = int(input())b = a[p - 1:q]total = 0for i in b:    total += int(i)print(total)
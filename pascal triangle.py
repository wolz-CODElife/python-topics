
from math import factorial as fc

def cmb(a, b):
    numerator = fc(a)
    denominator = fc((a-b)) * fc(b)
    return int(numerator / denominator)

def pascal(n):
    lst = []
    for i in range(n+1):
        lst.append(cmb(n, i))
    return lst

def fish(n):
    for i in range(n+1):
        for j in pascal(i):
            print(j, end=' ')
        print('\n')

import random as r
import math as m
from euler import euler_test

def solovey_strassen_test(p):
    k = int(r.random(2, 100)) # point -1( обрати k)
    counter = 0 # point 0( встановлюємо лічильник на 0)
    while counter < k:
        x = r.randint(2, p - 1) # point 1 // start
        if m.gcd(x, p) != 1:
            return bool(False)
        else:
            if euler_test(p, x) == bool(False):
                return bool(False)
            else:
                counter += 1
    return bool(True)
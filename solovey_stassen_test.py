import random as r
import math as m
from euler import euler_test

def solovey_strassen_test(p):
    k = r.randint(2, 1000) # point -1
    counter = 0 # point 0
    while counter < k:
        x = r.randint(2, p - 1) # point 1 // start
        if m.gcd(x, p) != 1:
            return ('Число складене')
        else:
            if euler_test(p, x) == bool(False):
                return ('Число складене')
            else:
                counter += 1
    return ('Число просте')
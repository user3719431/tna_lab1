import math as m
import random as r

def func(x):
    return pow(x, 2) + 1

def floyd(n, x = 2):
    x = 2
    counter = 1
    if m.gcd(((2 * counter) * func)(x) - (counter * func)(x), n) == 1:
        return m.gcd(((2 * counter) * func)(x) - (counter * func)(x), n)
    else:
        counter += 1
    floyd(n, r.randint(3, 100))
        
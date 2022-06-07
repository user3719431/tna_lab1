import numpy as np
import math as m
import test_div

def check_prime(n): #2а
    for i in range(2, int(m.sqrt(n))):
        if m.gcd(i, n) != 1:
            return bool(False) #якщо складене, йдем на крок 2б
    return bool(True) #якщо просте, повертаєм і завершуєм роботу

def div(n): #2б
    for i in range(2, 47):
        if m.gcd(i, n) != 1:
            print(m.gcd(i, n))
            algorythm(n / 2)
        else:
            pollard(n, x = 2)

def func_pollard(x): #2г
    return (pow(x, 2) + 1)

def pollard(n): #2г
    x = 2
    for i in range(1, 10000):
        if m.gcd(((2 * i) * func_pollard)(x) - (i * func_pollard)(x), n) != 1:
            print(m.gcd(((2 * i) * func_pollard)(x) - (i * func_pollard)(x), n))
            algorythm(n / m.gcd(((2 * i) * func_pollard)(x) - (i * func_pollard)(x), n)) #переходимо на 2в( ідентичний 2а)
    brilhart_morrison(n)

def brilhart_morrison(n): #2е
    

def algorythm(n):
    if check_prime(n) == bool(True):
        return (n + n)
    
    
    

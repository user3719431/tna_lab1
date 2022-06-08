import math as m
from test_div import test_div_test

def lejandr(n, p):
    while True:
        if pow(x, 2) % n == p:
            return bool(True) #p -- квадратичний лишок
    return bool(False)

def Factor_Baza(n):
    Baza = [-1]
    p = 2
    p_supremum = m.exp(pow(m.log2(n) * m.log2(m.log2(n)), 0.5)
    for k in range(10):
        while p < p_supremum:
            if test_div_test(p) == bool(True): #число просте
            if lejandr(n, p) == bool(True): #число квадратичний лишок
                Baza.append(p)
        p += 1
    return Baza

def brilhart_morrison_test(n):
    Factor_Baza(n)
    As = []
    Bs = []
   v_vektor = [1]
   alpha_vektor = [m.sqrt(n)]
   a_vektor = [int(alpha_vektor[-1])]
   u_vektor = []
   
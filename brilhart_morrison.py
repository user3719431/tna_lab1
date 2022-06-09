import math as m
from test_div import test_div_test
import random as r

def check_test(a, b, n):
    if a * b == n:
        return bool(True)
    else:
        return bool(False)

def lejandr(n, p):
    for x in range():
        if pow(x, 2) % n == p:
            return bool(True) #p -- квадратичний лишок
    return bool(False)

def Factor_Baza(n):
    Baza = [-1]
    p = 2
    p_supremum = m.exp(pow((m.log(n) * m.log(m.log(n))), 0.5))
    for k in range(10):
        while p < p_supremum:
            if test_div_test(p) == bool(True): #число просте
                if lejandr(n, p) == bool(True): #число квадратичний лишок
                    Baza.append(p)
        p += 1
    return Baza

def brilhart_morrison_test(n, alpha = (1 / m.sqrt(2))):
    Factor_Baza(n) #створили факторну базу
    As = [] # 1 рядок таблиці, куди війдуть значення a
    Bs = [0, 1] # 2 рядок таблиці, куди війдуть значення b
    B2s = [1] # 3 рядок таблиці, куди війдуть значення b^2
    v_vektor = [] # значення v
    alpha_vektor = [] # значення alpha
    a_vektor = [] # значення a
    u_vektor = [] # значення u
    
    #задаєм початкові значення
    v_vektor.append(1) # v0
    alpha_vektor.append(m.sqrt(n)) # alpha0
    a_vektor.append(int(alpha_vektor(-1))) # a0
    u_vektor.append(a_vektor[-1])
    # вираховуєм всі значення v, alpha, a, u
    for i in range(11):
        v_vektor.append((n - pow(u_vektor[-1], 2)) / v_vektor[-1])
        alpha_vektor.append((alpha_vektor[0] + u_vektor(-1)) / v_vektor[-1])
        a_vektor.append(int(alpha_vektor[-1]))
        u_vektor.append(a_vektor[-1] * v_vektor[-1] - u_vektor[-1])
    As = a_vektor # записали повністю 1 рядок таблиці
    Bs.pop(0) # видаляємо 0, тобто b_{-2}
    for i in range(len(As)):
        Bs.append(As[i] * Bs[i+1] + Bs[i])
    for i in range(len(Bs)):
        B2s.append(pow(Bs[i], 2) % n)
    list = [i for i, x in enumerate(B2s) if B2s.count(x) > 1] # значення повторів
    
    X = 1
    Y = 1
    
    for i in range(len(list)):
        X *= Bs[list[i]]
        Y *= B2s[list[i]]
    
    gcd1 = m.gcd(X + Y, n)
    gcd2 = m.gcd(X - Y, n)
    if check_test(gcd1, gcd2) == bool(True):
        return gcd1, gcd2
    else:
        brilhart_morrison_test(n, r.randint(2, 10))
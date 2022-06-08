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

def brilhart_morrison_test(n, alpha = (1 / m.sqrt(2))):
    Factor_Baza(n) #створили факторну базу
    As = [] # 1 рядок таблиці, куди війдуть значення a
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
    
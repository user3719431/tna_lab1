import math as m

def yakobi(a, n, k):
    if a < 0:
        k *= pow(-1, (n - 1) // 2)
        yakobi(-a, n, k)
    if a % 2 == 0:
        k *= (-1) ** ((pow(n, 2) - 1) / 8)
        yakobi(a / 2, n, k)
    if a == 1:
        return k
    if a < n:
        k *= pow(-1, ((n - 1)(a - 1)) / 4)
        yakobi(n % a, a, k)
        
                    

def euler_test(p, x):
    if pow(x, (p - 1) / 2) % p == yakobi(x, p, k = 1):
        return bool(True)
    elif pow(x, (p - 1) / 2) % p - p == yakobi(x, p, k = 1):
        return bool(True)
    else:
        return bool(False)
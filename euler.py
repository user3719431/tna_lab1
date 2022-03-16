import math as m

def euler_test(p, x):
    if m.gcd(p, x) == 1:
        if pow(x, (p - 1) // 2) % p == 1 or (p - 1):
            return bool(True)
        else:
            return bool(False)
    else:
        return bool(False)
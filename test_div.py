import math

def test_div_test(p):
    for i in range (1, math.sqrt(p)):
        if p % i == 0:
            return bool(False)
        else:
            return bool(True)
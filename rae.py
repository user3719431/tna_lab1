import math

def rae(a, b):
    	return abs(a) if b == 0 else gcd(b, a % b)
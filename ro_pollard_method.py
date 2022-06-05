from random import randint
from fractions import gcd

def f(x, N):
  return (x**2 - 1) // N
N = int(input())
global i
i = 0
global x0
x0 = randint(10,N-1)

def fun(N):
    y0 = x0
    arr = [x0]
    a = [y0]
    i += 1
    arr[i] = f(arr[i-1], N) // N
    a[i] = f(f(a[i-1], N), N) // N
    d = gcd(abs(arr[i]-a[i]), N)
    if d == 1:
        return fun(N)
    elif d == N:
        return 'факторизация не удалась'
    else:
        return d
print(fun(N))
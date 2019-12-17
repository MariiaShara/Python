from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


print(fibo_gen())

z = 1
for el in fibo_gen():
    if z > 15:
        break
    else:
        print(el)
        z += 1

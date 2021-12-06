from math import *

n = input()

n = int(n)

c = int(floor(n/3))


v = c
az = c
am = c

if c == 0:
    if n >= 1:
        v = v+1
    if n >= 2:
         az = az+1
    if n == 3:
         am = am+1
else:
    if n%3 >= 1:
        v = v+1
    if n%3 >= 2:
         az = az+1
    if n%3 == 3:
         am = am+1
    
print("Vermelho",v)
print("Azul", az)
print("Amarelo", am)
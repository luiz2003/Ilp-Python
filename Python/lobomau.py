from math import *

t, d = input().split()
t = int(t)
d = int (d)

v, p = input().split()
v = int(v)
p = int(p)

c = t*v + p*(int(floor(t/d)))

print(c)
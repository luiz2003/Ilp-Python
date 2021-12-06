x = input()
x = int(x)
p = float(0.0)
for i in range(x):
    h = input()
    h = float(h)
    p+= h
r = p/3
a = "{:.2f}".format(r)
print(a)
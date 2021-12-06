p, c, a = input().split()

p = int(p)
c = int(c)
a = int(a)

if p*c >= a:
    print("S")
else:
    print("N")
n,x,xpMin = input().split()
n = int(n)
x = int(x)
xpMin = int(xpMin)
for i in range(n):
    xp,q = input().split()
    
    xp = int(xp)
    q = int(q)

    if xp>= xpMin:
        print(xp + x, q + 1)
    else:
        print(xp,q)

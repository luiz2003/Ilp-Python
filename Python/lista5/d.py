n,m = input().split()

n = int(n)
m = int(m)

spc = []

for i in range(n):
    aux = [int(x) for x in input().split()]
    
    spc.append(aux)

c = 0

for i in range (m):
    x,y = input().split()
    x = int(x)
    y = int(y)
    
    for i in range(x+1):
        if x - i >= 0 and spc[x-i][y] == 1:
            c+= 1
            spc[x-i][y] = 0
            break

print(c)
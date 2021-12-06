n,m = input().split()

n = int(n)
m = int(m)

m1 = ['']*n

for i in range(n):
    m1[i] = [int(x) for x in input().split()]

m2 = ['']*n

for i in range(n):
    m2[i] = [int(x) for x in input().split()]

mr = []*n
for i in range(n):
    aux = []

    for k in range(m):
        aux.append(m1[i][k] - m2[i][k])
    
    mr.append(aux)

    for j in range(m):
        print(mr[i][j], end= " ")
    
    print('')
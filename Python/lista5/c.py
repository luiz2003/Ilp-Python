n = int(input())

matriz = []

for i in range(n):
    aux = [int(x) for x in input().split()]

    matriz.append(aux)

x, y = input().split()

hx = int(x)
ry = int(y)

if hx <= ry:
    h = sum(matriz[hx]) - matriz[hx][ry]
    r = 0
    for i in range(n):
        r += matriz[i][ry]
else:
    h = sum(matriz[hx])
    r = 0
    for i in range(n):
        if i != hx:
            r += matriz[i][ry]

print("Harry", h)
print("Ron", r)

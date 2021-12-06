f = input()

matriz = []

fre = False

for i in range(10):
    matriz.append(input().split())
    for j in matriz[i]:
        if j == f:
            fre = True

print("sim") if fre else print("nao")
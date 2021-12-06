n = int(input())

indexes = [0]*1000001
unsorted = [int(x) for x in input().split()]

maior = -1
for x in unsorted:
    indexes[x] = 1
    if x>maior:
        maior = x

resposta = ""
for i in range(maior+1):
    if indexes[i]==1:
        resposta += str(i) + " "

print(resposta)
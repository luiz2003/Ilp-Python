n, m = input().split()

n = int (n)

m = int(m)

maior = -1


for i in range(n):
    sum = 0
    cinto = input().split()
    for num in cinto:
        p = int(num)
        sum += p
    if sum > maior:
        maior = sum
    
print(maior)
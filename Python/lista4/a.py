n = input()

n = int(n)

itens = [ int(x) for x in input().split()]

out = []

for i in range(n):
    out.append(itens[(n-1)-i])
    print(out[i],end=" ")
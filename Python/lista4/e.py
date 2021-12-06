n,p = input().split()
n = int (n)
p = int(p)

rocks = [0]*p

s = []

for i in range(n):
    s.append(int(input()))

for f in s:
    pf = 0
    while pf<p :
        rocks[pf] = 1
        pf += f

for r in rocks:
    print(r,end=" ")

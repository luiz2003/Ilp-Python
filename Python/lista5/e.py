n, m = input().split()

n = int(n)
m = int(m)

c = 0

for i in range(n):
    l = [int(x) for x in input().split()]
    for i in l:
        c+=i
        if c < 0:
            c = 0

print(c)
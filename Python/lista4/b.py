n = int(input())

emeralds = [ int(x) for x in input().split()]

c = int(input())

for i in range(n):
    if emeralds[i]==c:
        print(c)
        exit()
print('-1')
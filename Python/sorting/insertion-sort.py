list = [int(x) for x in input().split()]

n = len(list)

for start in range(1,n):
    i = start
    while i >= 1 and list[i] < list[i - 1]:
        list[i], list[i-1] = list[i-1], list[i]
        i -= 1

print(list)

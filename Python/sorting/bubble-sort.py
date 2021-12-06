list = [int(x) for x in input().split()]

#bubble sort
n = len(list)

for end in range(n-1, 0, -1):
    for i in range(0, end):
        if list[i] > list[i+1]:
            list[i], list[i + 1] = list[i+1], list[i]

print(list)

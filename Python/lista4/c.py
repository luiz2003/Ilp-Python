n =  int(input())

s = [int(x) for x in input().split()]
sum = 0
for i in range(n):
    sum+=s[i]

find = sum/2
sum = 0

for i in range(n):
    sum+=s[i]
    if sum == find:
        res = i+1
        print(res)
        break
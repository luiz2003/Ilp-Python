n = input()

list = [int(x) for x in input().split()]

list.sort()

res =""
for i in range(8) :
    res+= str(list[i]) + " "

print(res)
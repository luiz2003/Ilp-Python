list = [int(x) for x in input().split()]

n = len(list) 

for end in range(n-1, 0 ,-1):
  maxInd = 0
  for i in range(1,end+1):
    if list[i] < list[maxInd]:
      maxInd = i
  list[maxInd], list[end] = list[end], list[maxInd]

print(list)

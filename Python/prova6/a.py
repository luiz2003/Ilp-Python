k =  int(input())

list =[]
for i in range(k):
    list.append(int(input()))

n = len(list)

for end in range(n-1, 0 ,-1):
  maxInd = 0
  for i in range(1,end+1):
    if list[i] > list[maxInd]:
      maxInd = i
  list[maxInd], list[end] = list[end], list[maxInd]

for i in list :
    print(i)

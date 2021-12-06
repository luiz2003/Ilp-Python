n, m = input().split()

n = int(n)

m = int(m)

photo = [-1] # -inf

for i in range(n):
    photo += [int(x) for x in input().split()]

photo += [1001] # inf

photo.sort()

q = int(input())

cnslt  = [int(x) for x in input().split()]

def findLast(x):
    start = 1
    end = n*m
    while start <= end:
        mid = (start + end)//2
        if photo[mid] - x <= 0 and photo[mid+1] - x >0 :
            return mid 
        elif photo[mid] - x > 0:
            end = mid - 1
        elif photo[mid] - x <= 0 and photo[mid + 1] -  x <= 0:
            start = mid + 1
    return 0 

for i in cnslt:
    print(findLast(i))

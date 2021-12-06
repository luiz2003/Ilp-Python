def stirling1(n,k):
    if (k>0 and n == 0) or (n>0 and k == 0) :
        return 0
    elif n == k:
        return 1
    else:
        return stirling1(n-1,k-1) + (n-1)*stirling1(n-1,k)

def stirling2(n,k):
    if k == 0 or 1<n<k:
        return 0
    elif k == 1 or k == n:
        return 1
    else:
        return stirling2(n-1, k-1) + k*stirling2(n-1,k)

s = int(input("Choose your Stirling Order (1 or 2):  "))
n,k = input("Choose your n and k: ").split()

n = int(n)
k = int(k)

if s == 1:
    print(stirling1(n,k))
elif s == 2:
    print(stirling2(n,k))
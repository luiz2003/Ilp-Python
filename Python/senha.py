n,a,b = input().split()
n = int(n)
a = int(a)
b = int(b)
c = 0
impares = []

for i in range(a,b+1):
    if (a+c)%2==1:
        impares.append(a+c)
    c+=1

if len(impares)<n:
    print("Falhamos galera")
else:
    for i in range(n):
        print(impares[i],end="")
    print("\n",end="")
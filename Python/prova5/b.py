n,m =  input().split()

n = int(n)
m = int(m)

board = []

b = 0

for i in range (n):
    aux = [int(x) for x in input().split()]
    for j in aux:
        if j == 1:
            b+=1

    board.append(aux)

a =  int(input())

t = 0
for i in range(a):
    x,y = input().split()
    x = int(x)
    y = int(y)


    if x<=n and y<=m and y>=1 and board[x-1][y-1]==1 :
        t+=1
        board[x-1][y-1] = 0


print("HASTA LA VISTA BABY") if t == b and b!=0 else print("ILL BE BACK")
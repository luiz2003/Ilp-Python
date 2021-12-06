board = []

for i in range(7):
    aux = [int(x) for x in input().split()]
    board.append(aux)

c = 0

for i in range(7):
    for j in range(7):
        if board[i][j] == 1:
            c+=1
           
            board[j][i] = 0

print(c)
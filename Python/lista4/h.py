n =  int(input())

names = []

for i in range (n):
    names.append(input().title().split())


for i in range(n):
    for j in range (len(names[i])):
        if j  < (len(names[i]) -1) :
            names[i][j] = names[i][j][0]+"." #formate com o if aqui
        print(names[i][j], end= " ")
    print('')
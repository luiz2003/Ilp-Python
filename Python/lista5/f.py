map = []

for i in range(10):
    aux = [x for x in input().split()]

    map.append(aux)

def verI(i,j,v):
    if map[i][j]  == 't':
        if map[i+v][j] == '*':
            map[i][j] = 'p'
            return True
    
    return False

def verJ(i,j,v):
    if map[i][j] == 't':
        if map[i][j+v] == '*':
            map[i][j] = 'p'
            return True
    
    return False

for i in range(10):
    for j in range(10):
        if  i+1 < 10 :
            if verI(i,j,1):
                continue
        if  i-1 >= 0:
            if verI(i,j,-1):
                continue
        if j+1 < 10:
            if verJ(i,j,1):
                continue
        if j-1 >= 0:
            if verJ(i,j,-1):
                continue

for i in range(10):
    for j in range(10):
        print(map[i][j],end=' ')
    print('')
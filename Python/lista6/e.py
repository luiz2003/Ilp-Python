n = int(input())

cat = []

for i in range(n):
    aux = input()
    cat.append(aux)

def searchAnimal(animal):
    ini = 0 
    fim = n -1

    while ini <= fim :
        mid = (ini + fim)//2

        if cat[mid] == animal :
            return animal + " vive!"
        elif animal < cat[mid]:
            fim = mid - 1
        elif animal > cat[mid] :
            ini = mid + 1
    
    return animal + " foi extinto :("

q = int(input())

for i in range(q):
    animal = input()
    print(searchAnimal(animal))
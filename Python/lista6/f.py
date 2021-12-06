n = int(input())

gen = [x for x in input().split()]

m = int(input())

frbd = [x for x in input().split()]

c = int(input())

spl = [x for x in input().split()]

def searchSpl(x):
    start = 0
    end = m-1

    while start <= end:
        mid = (start+end)//2
        if frbd[mid] == x:
            return "Proibido"
        elif x < frbd[mid]:
            end = mid - 1
        elif x > frbd[mid]:
            start = mid + 1
    return "Geral"

for x in spl:
    print(searchSpl(x))
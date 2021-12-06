t = int(input())
aux = 0
while(True):
    p = int(input())
    
    if p == 0:
        break
    if p > t:
        aux = 1

if aux == 0:
    print("O Havai pode dormir tranquilo")
else:
    print("ALARME")

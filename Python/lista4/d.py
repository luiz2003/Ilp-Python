n = int(input())

lvls = [int(x) for x in input().split()]

maxHp = int(input())

hp = maxHp

for x in lvls:
    if x>1 :
        hp-=x
        if hp <= 0:
            print("You Died")
            exit()
    if x == 1:
        hp = maxHp

print("Yes, you can")
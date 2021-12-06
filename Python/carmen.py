x = input()
y = input()

x = int(x)
y = int(y)

if x >= 0 and y != 0:
    if y >= 0:
        print("Quadrante 1")
    else:
        print("Quadrante 4")

elif x < 0 :
    if y >= 0:
        print("Quadrante 2")
    else:
        print("Quadrante 3")

if x == 0 and y == 0 :
    print("Centro")
n1, n2, n3, n4, n5, n6  = input().split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

p = n1 + n2 + n3 + n4 + n5 + n6

if p >= 250:
    print("S+")
elif p >= 200:
    print("S")
elif p >= 180:
    print("S-")
elif p >= 150:
    print("A+")
elif p >= 100:
    print("A")
elif p >= 80:
    print("A-")
elif p >= 60:
    print("B+")
elif p >= 40:
    print("B")
else:
    print("B-")
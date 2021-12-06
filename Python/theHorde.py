q = input()
q = int(q)

m = 0.0
for i in range(q):
    p = input()
    p = float(p)
    if i<=q-2:
        m += 0.05*p
    else:
        if p <=m:
            print("Escolheu o seu destino!")
        else:
            print("Fez de mim o que eu sou!")

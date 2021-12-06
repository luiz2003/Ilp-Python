e, p = input().split()

e = int(e)
p = int(p)
c = 0
c = int(c)

while(e>0 and p>0):
    e = e-p
    p = p-1
    c = c+1

if(e<=0):
    print(c)
else:
    print("F")
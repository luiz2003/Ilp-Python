c, o, l, x = input().split()
p = 0
c = int(c)
o = int(o)
l = int(l)
x = int(x)

menor = min(c//4,o//8,l//2,x)

if menor == c//4:
    p = c//4
elif menor == o//8:
    p = o//8
elif menor == l//2:
    p = l//2
else:
    p = x

t = p*1259

s = t%60
h = t//(60*60)
m = (t//60) - h*60

h = str(h)
m = str(m)
s = str(s)

print(h+" h",m+" m",s+" s")
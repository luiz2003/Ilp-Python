t = int(input())

s = t%60
h = t//(60*60)
m = (t//60) - h*60

h = str(h)
m = str(m)
s = str(s)


print(h+"h",m+"m",s+"s")
phrase = input()

x , target = input().split()

string = phrase.replace(" ", "")

x = int(x)

c = string.count(target)

print(c)

if c == x:
    print("SIM!")
else:
    print("NAO!")
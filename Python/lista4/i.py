st = input()

st = st.lower().replace(" ", "")

revSt = st[::-1]

for i in range(len(st)):
    if st[i] != revSt[i]:
        print("!Palindromo")
        exit();

print("Palindromo")
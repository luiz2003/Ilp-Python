n = input()

n = int (n)

men = [int(x) for x in input().split()]
women = [int(x) for x in input().split()]

men.sort(reverse=True)
women.sort()

for i in range(n):
    print(men[i], women[i])
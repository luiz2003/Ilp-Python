n = input()
n = int(n)

planets = []

for i in range(n):
    planet = [int(x) for x in input().split()]
    planets.append(planet)

def planetCompare(e):
    return e[1]
    
planets.sort(reverse=True, key=planetCompare)

for planet in planets:
    print(planet[0],planet[1])
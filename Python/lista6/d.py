q,c,o = input().split()

q = int(q)

pokemons = []

for i in range(q):
    pokemon = [x for x in input().split()]
    pokemon[1] = int(pokemon[1])

    pokemons.append(pokemon)

if c == 'N':
    def compareName(e):
        return e[0]
    if o == 'C':
        pokemons.sort(key=compareName)
    else:
        pokemons.sort(reverse=True, key=compareName)
elif c == 'L':
    def comapareLvl(e):
        return e[1]
    if o == 'C':
        pokemons.sort(key=comapareLvl)
    else:
        pokemons.sort(reverse=True, key=comapareLvl)

for pokemon in pokemons:
    print(pokemon[0],pokemon[1])
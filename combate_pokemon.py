
pokemon_enemigo = input("Elige un pokemon para combatir (Bulbasaur / Charmander / Squirtle): ")

vida_pikachu =100
vida_enemigo = 0

while pokemon_enemigo != "Bulbasaur" and pokemon_enemigo != "Charmander" and pokemon_enemigo != "Squirtle":
    pokemon_enemigo = input("Elige un pokemon para combatir (Bulbasaur / Charmander / Squirtle): ")


if pokemon_enemigo == "Bulbasaur":
    vida_enemigo = 100
    ataque_enemigo = 8
    nombre_pokemon = "Bulbasaur"

elif pokemon_enemigo == "Charmander":
    vida_enemigo = 80
    ataque_enemigo = 12
    nombre_pokemon = "Charmander"

elif pokemon_enemigo == "Squirtle":
    vida_enemigo = 90
    ataque_enemigo = 10
    nombre_pokemon = "Squirtle"

while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("Elige un ataque (Chispazo / Rayo): ")
    ataque_pikachu = 0

    if ataque_elegido == "Chispazo":
        ataque_pikachu = 10
        vida_enemigo -= ataque_pikachu

    elif ataque_elegido == "Rayo":
        ataque_pikachu = 15
        vida_enemigo -= ataque_pikachu
    else:
        ataque_elegido = "descanso"
        ataque_pikachu == 0

    print("Pikachu usa {} y causa {} de daño.".format(ataque_elegido,ataque_pikachu ))

    print("La vida de {} es de {}.".format(nombre_pokemon, vida_enemigo))

    print("{} usa el ataque basico y causa {} de daño.".format(nombre_pokemon, ataque_enemigo))

    vida_pikachu -= ataque_enemigo

    print("La vida de pikachu es de {}.".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")

if vida_pikachu <= 0:
    print("¡Has perdido!")


print("El combate ha terminado.")
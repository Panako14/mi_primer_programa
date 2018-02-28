frase_usuario = input("Escribe una frase: ")

vocales_a_cambiar = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for valor in vocales_a_cambiar:
     frase_usuario = frase_usuario.replace(valor, "{}")

posicion = 1
for valor in frase_usuario:
    frase_usuario = frase_usuario.replace("{}", str(posicion), 1)
    posicion += 1


print(frase_usuario)
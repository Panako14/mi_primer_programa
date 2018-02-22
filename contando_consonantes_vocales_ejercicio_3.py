texto_usuario = input("Escribe una frase: ")

vocales =  ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
lista_vocales = []

for letras in texto_usuario:
    if letras in vocales:
        lista_vocales.append(letras)

print("Vocales = {}".format(lista_vocales))

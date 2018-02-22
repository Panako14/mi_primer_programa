texto_usuario = input("Escriba una frase: ")

espacio = [" "]
puntos = ['.']
comas = [","]

n_espacio = 0
n_puntos = 0
n_comas = 0

for simbolo in texto_usuario:
    if simbolo in espacio:
        n_espacio += 1
    if simbolo in puntos:
        n_puntos += 1
    if simbolo in comas:
        n_comas += 1

print("Espacios = {}".format(n_espacio))
print("Puntos = {}".format(n_puntos))
print("Comas = {}".format(n_comas))
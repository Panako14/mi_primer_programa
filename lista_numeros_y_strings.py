lista_usuario = ["casa", "cueva", 1, 2, 3, "teclado", 7.5]
lista_numeros = []
lista_strings = []

for dato in lista_usuario:
    if type(dato) == int or type(dato) == float:
        lista_numeros.append(dato)
    elif type(dato) == str:
        lista_strings.append(dato)

print(lista_numeros)
print(lista_strings)
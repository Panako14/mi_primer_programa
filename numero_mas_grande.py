
lista = [1, 2, 3, 12, 5, 20, 7, 8, 70, 10, 11, 12, 13, 14]

numero_mas_grande = lista[0]

for numero in lista:
    if numero > numero_mas_grande:
        numero_mas_grande = numero

print(numero_mas_grande)



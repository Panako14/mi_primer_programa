lista_numeros = [5, 56, 83]


def numero_mas_grande(lista):

    numero_mas_grande = lista_numeros[0]

    for item in lista:
        if numero_mas_grande < item:
            numero_mas_grande = item
    return numero_mas_grande


print(numero_mas_grande(lista_numeros))

lista_numeros = [5, 56, 8]

def numero_mas_grande(lista):

    numero = lista_numeros[0]

    for item in lista:
        if numero < item:
            numero = item

    print(numero)

numero_mas_grande(lista_numeros)


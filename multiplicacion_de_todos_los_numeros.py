lista_usuario = [1, 2, 3, 4, 5, 6]
lista_numeros = []

for dato in lista_usuario:
    lista_numeros.append(int(dato))


resultado = 1

for numero in lista_numeros:
     resultado *= numero

print(resultado)
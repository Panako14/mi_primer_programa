lista_numeros = []
numero_usuario = ""

while not numero_usuario.isdigit():
    numero_usuario = input("Dime un número (Escribe FIN para terminar): ")
    if numero_usuario == "FIN":
        break
    lista_numeros.append(int(numero_usuario))
    print("Número añadido.")
    numero_usuario = ""

total_suma = 0

for numero in lista_numeros:
    total_suma += numero

media = total_suma / len(lista_numeros)

print("La media de esos números es {}".format(media))

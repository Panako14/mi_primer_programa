lista_usuario = []
numero_usuario = ""
while len(lista_usuario) < 10:
    while not numero_usuario.isdigit():
        numero_usuario = input("Dime un número: ")
    lista_usuario.append(int(numero_usuario))
    numero_usuario = ""
    print("Número añadido.")

numero_pequeño = lista_usuario[0]

for item in lista_usuario:
    if item < numero_pequeño:
        numero_pequeño = item
print("El número más pequeño es {}".format(numero_pequeño))

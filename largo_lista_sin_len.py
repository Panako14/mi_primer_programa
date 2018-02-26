lista = []
largo_lista = 0
numero_usuario = ""


while not numero_usuario.isdigit():
    numero_usuario = input("Dime un número(Escribe FIN para terminar): ")
    if numero_usuario == "FIN":
        break
    lista.append(int(numero_usuario))
    largo_lista += 1
    numero_usuario = ""
    print("Número añadido.")
print("El largo de la lista es {}".format(largo_lista))

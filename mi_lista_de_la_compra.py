mi_lista = []

que_comprar = input("¿Que necesito comprar? (Escribe FIN para terminar): ")

while que_comprar != "FIN":
    mi_lista.append(que_comprar)
    que_comprar = input("¿Que mas necesito? (Escribe FIN para terminar): ")

largo_lista = len(mi_lista)
indice_lista = 0

while indice_lista < largo_lista:
    print("Necesito {}".format(mi_lista[indice_lista]))
    indice_lista += 1

print("Esta es mi lista de la compra.")




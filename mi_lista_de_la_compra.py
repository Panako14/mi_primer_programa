mi_lista = []

que_comprar = input("¿Que necesito comprar? (Escribe FIN para terminar): ")

while que_comprar != "FIN":
    mi_lista.append(que_comprar)
    que_comprar = input("¿Que mas necesito? (Escribe FIN para terminar): ")

for item in mi_lista:
    print("Necesito comprar {}".format(item))

print("Esta es mi lista de la compra.")




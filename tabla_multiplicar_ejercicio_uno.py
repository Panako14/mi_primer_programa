numero_tabla = int(input("De que número quieres saber la tabla: "))
for multiplo in range(1, 11):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))

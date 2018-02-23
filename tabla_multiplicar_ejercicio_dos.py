numero_tabla = int(input("De que numero quieres la tabla: "))
for numero in range(1, 11):
    if numero % 2 == 0:
        print("{} x {} = {}".format(numero_tabla, numero, numero_tabla * numero))
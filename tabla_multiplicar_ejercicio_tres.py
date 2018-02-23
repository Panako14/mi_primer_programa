numero_tabla = int(input("De que numero quieres la tabla: "))
for numero in reversed(range(1, 11)):
    print("{} x {} = {}".format(numero_tabla, numero, numero_tabla * numero))
lista = [20, 32, 54, 67, 30, 70, 28, 35, 25, 90, 89, 42]

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

for numero in lista:
    if numero % 2 == 0:
        multiplos_dos.append(numero)
    if numero % 3 == 0:
        multiplos_tres.append(numero)
    if numero % 5 == 0:
        multiplos_cinco.append(numero)
    if numero % 7 == 0:
        multiplos_siete.append(numero)

print("Multiplos de dos = {} ".format(multiplos_dos))
print("Multiplos de tres = {} ".format(multiplos_tres))
print("Multiplos de cinco = {}".format(multiplos_cinco))
print("Multiplos de siete = {}".format(multiplos_siete))


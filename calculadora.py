operacion = input("¿Que operacíon quieres realizar? (multiplicar / dividir / sumar/ restar)")


primer_numero = int(input("Primer número: "))

segundo_numero = int(input("Segundo número: "))

if operacion == "multiplicar":
    resultado_operacion = primer_numero * segundo_numero
elif operacion == "dividir":
    resultado_operacion = primer_numero / segundo_numero
elif operacion == "sumar":
    resultado_operacion = primer_numero + segundo_numero
elif operacion == "restar":
    resultado_operacion = primer_numero - segundo_numero

print ("Resultado: {}".format(resultado_operacion))
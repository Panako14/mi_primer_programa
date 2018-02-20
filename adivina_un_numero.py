
number_to_guess = 2

user_number = int(input("Adivina un numero: "))

if user_number == number_to_guess:
     print('Has ganado')
else:
    second_try = int(input("Intentalo de nuevo: "))
    if second_try == number_to_guess:
        print("Has ganado")
    else:
        third_try = int(input("Intentelo de nuevo: "))
        if third_try == number_to_guess:
            print("Has ganado")
        else:
            fourth_try = int(input("Intentelo se nuevo: "))
            if fourth_try == number_to_guess:
                print("Has ganado")
            else:
                fifth_try = int(input("Intentelo de nuevo: "))
                if fifth_try == number_to_guess:
                    print("Has ganado")
                else:
                    print("Has perdido")

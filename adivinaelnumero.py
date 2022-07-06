import random


def adivina_el_numero(x):

    print("======================")
    print ("Bienvenido al juego ")
    print("======================")
    print("Tu meta es adivinar el numro generado por la computadora.")


    numero_aleatorio = random.randint(1, x) # numero aleatorio entre 1 y x
    prediccion = 0

    while prediccion != numero_aleatorio:
        # el usuario ingresa un numero
        prediccion = int(input(f"adivina un numero entre 1 y {x}: ")) # f-string

        if prediccion < numero_aleatorio:
            print("intenta otra vez, Este numero es muy pequeno.")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez, Este numero es muy grande.")    

    print(f"felicidades , adivinaste en numer `{numero_aleatorio} correctamente.")


adivina_el_numero(10)



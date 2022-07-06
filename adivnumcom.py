import random

def adivina_el_numero_computadora (x):

    print("======================")
    print ("Bienvenido al juego ")
    print("======================")
    print(f"selecciones un numero entre 1 y {x} para que la computadora intente adivinarlo..")

    limite_inferior = 1 
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
               
        respuesta = input(f"Miprediccion es {prediccion}.si es muy alta ingresa (A).si es muy baja ingresa (B). si es correcta ,ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1


    print(f"siii! la computadora adivino tu nimero correctamente:{prediccion}")
    
adivina_el_numero_computadora(10)    



    

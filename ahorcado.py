from operator import le
import random 
import string  

from palabras import palabras
from ahorcado import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    #seleccionar una palabra al azar de la lista 
    #de palabras vaçlidas.
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()    

def ahorcado():

    print("====================================")
    print(" !Bienvenido al juego del ahorcado !")
    print("====================================")  

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
     
    vidas = 7 

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")


  #MOSTRAR EL ESTADO  actuar de la palabra 
  # H - L A
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"P alabras:{'-'.join(palabra_lista)}")

        letra_usuario = input("escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:letras_adivinadas.add(letra_usuario)

             if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            # Si la letra no está en la palabra, quitar una vida.
             else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        # Si la letra escogida por el usuario ya fue ingresada.  elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

            if vidas == 0: 
                print(vidas_diccionario_visual[vidas])
                print(f"!ahorcado! perdiste.lo lamento mucho la palabra era {palabra}")
            else:
                print(f'! excelente ! ! adivinaste la palabra {palabra}')  

    if__name__=='__main__':
    ahorcado()


           

       


import random


def jugar():
    usuario = input("Escoge una opcion : 'pi' para piedra, 'pa' para papel, 'ti' para tiujeras.\n").lower()
    computadorta = random.choice (['pi' , 'pa' ,'ti'])

    if usuario == computadorta:
        return ' ! Empate !'

    if gano_el_jugador(usuario, computadorta):
        return '!Ganaste !'

    return '!perdiste!'


def gano_el_jugador(jugador, oponente):




     if (( jugador == 'pi' and oponente == 'ti')
         or (jugador =='ti' and oponente == 'pa')
         or (jugador =='pa' and oponente == 'pi')):

         return True
     else:
         return False



print(jugar ())


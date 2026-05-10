import random

def pedirNumeroTablero(nombreJugador):
    ## primer run
    while True:
        try:
            ## se le pide el numero del tablero al user
            tamañoTablero = int(input(f"ingrese el tamaño del tablero, entre 5 y 25 para: {nombreJugador} "))
            if 5 <= tamañoTablero <= 25:
                return tamañoTablero
            else:
                print("el tablero tiene que ser de entre 5 y 25")
        except:
            print("ingrese un numero válido")

## se hace una tirada del 1 al 6 para los dados
## dspues se le suma la posicion y se muestra en consola
def moverJugador(nombreJugador, posicion):
    tirada = random.randint(1,6)
    posicion = posicion + tirada
    print(f"{nombreJugador} saco {tirada}!! - Posición actual: {posicion}")
    return posicion

primerJugador = input("nombre del primer jugador?: ")
segundoJugador = input("nombre del segundo jugador? : ")

tableroJugador1 = pedirNumeroTablero(primerJugador)
tableroJugador2 = pedirNumeroTablero(segundoJugador)


## esta forma de hacer el tablero no se me hubiera ocurrido, le pedi a la IA que me ayude
tableroJugador1 = [primerJugador] + [0] * tableroJugador1
tableroJugador2 = [segundoJugador] + [0] * tableroJugador2

posicion1 = 0
posicion2 = 0
turno = 1
ganaron = False

while not ganaron:
    if turno == 1:
        print(f" turno de {primerJugador} ")
        posicion1 = moverJugador(primerJugador, posicion1)


        ## hay que corregir esto, se loopea con el usuario 1 
        if(posicion1) >= len(tableroJugador1) - 1:
            ## corregir condicion del if
            print(f"gano el jugador {primerJugador}!")
            ganaron = True
            turno = 2
    else:
            print(f"turno de {segundoJugador}")
            posicion2 = moverJugador(segundoJugador, posicion2)
    if(posicion2) >= len(tableroJugador2) - 1:
            print(f"gano el jugador {segundoJugador}!")
            ganaron = True
            turno = 1
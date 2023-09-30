import os
import keyboard
import time
from agenteInt import Agentes
from juego import Juego

global juego
global agI 
juego = 0
opcion = 0
puntaje = 0
intentos = 1
movimientos = 0
tablero = [[' ' for _ in range(5)] for _ in range(5)]
velocidad = 0.2

def nuevo_juego():
    global juego
    if juego == 0:
        juego = Juego(tablero)
        juego.tablero[4][0] = 'A'
    else:
        juego.reiniciar_juego()

    global agI 
    agI = Agentes('agI', [4,0])

    global gumpy 
    gumpy = Agentes('gumpy', juego.gumpy)

    global tesoro
    tesoro = juego.tesoro

    print('Ingrese la velocidad de turno(0 = alto, 1 = medio y 2 = bajo):')
    global velocidad
    velocidad = 3
    while velocidad < 0 or velocidad > 2:
        velocidad = int(input('Velocidad de juego:'))

def mostrar_menu():
    print("""\n¡¡¡Bienvenido a Encuentra el tesoro!!!
1. Continuar jugando
2. Nuevo juego
3. Salir""")
    
    global opcion 
    
    opcion = input('Ingrese su opcion:')

    match opcion:
            case "1":
                if juego == 0:
                    print('No tiene ningún juego comenzado.')
                    opcion = 0
                else:
                    if puntaje < -500 or puntaje > 500:
                        juego.reiniciar_juego()
                    juego.imprimir_tablero()

            case "2":
                nuevo_juego()

            case "3":
                exit()

            case default:
                opcion = 0
                print ('Vuelva a ingresar su opción')

# Bucle principal del juego
while True:
    #En caso de que no hayamos elegido una opción válida o hayamos puesto pausa, entonces mostraremos el menu
    if opcion == 0 or keyboard.is_pressed('p'):
        mostrar_menu()
    
    if juego != 0:
        
        if movimientos == 0:
            inicio = True 
        else:
            inicio = False
            tablero = agI.mover_agente(juego.tablero)
            if movimientos % 2 == 0:
                tablero = gumpy.mover_agente(juego.tablero)

        juego.imprimir_tablero()  

        print(agI.mostrar_stats(juego.tablero, inicio, puntaje))
        print(gumpy.mostrar_stats(juego.tablero, inicio, puntaje))

        # Verificar si el agente llegó al tesoro
        if (agI.posicion) == (tesoro):
            print("¡El agente ha encontrado el tesoro y ha ganado!")
            puntaje += 1000
            agI = Agentes('agI', [4,0])
            gumpy = Agentes('gumpy', juego.gumpy)
            agI.reiniciar_memoria()
            gumpy.reiniciar_memoria()
            mostrar_menu()
        
        # Verificar si el gumpy atrapó al agente
        if (agI.posicion) == (gumpy.posicion):
            print("¡El agente ha sido atrapado por el gumpy y ha perdido!")
            puntaje -= 1000
            intentos += 1
            movimientos = -1
            agI = Agentes('agI', [4,0])
            gumpy = Agentes('gumpy', juego.gumpy)
            agI.reiniciar_memoria()
            gumpy.reiniciar_memoria()
            mostrar_menu()
        
        print(f'Intentos: {intentos} \nMovimientos {movimientos} \nPuntaje: {puntaje}')
        movimientos += 1
        puntaje -= 1
    
    if(velocidad == 0):
        velocidad = 0.4
    time.sleep(velocidad)
    os.system('cls')


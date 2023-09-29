import os
import random

#ENTORNO
class Juego:
    tesoro = 0,0
    
    def __init__(self, tablero):
        self.tablero = tablero
        tablero[4][0] = 'A'
        self.gumpy = self.posicionar_objetos() 
        self.tesoro = tesoro
        
    # Función para imprimir el tablero
    def imprimir_tablero(self):
        print('\n' * 3)
        for fila in self.tablero:
            for casilla in fila:
                print('\t', '[ ', casilla, ' ]' ,end=' ')
            print('\n' * 3)
        

    def posicionar_objetos(self):
        objetos = {'P1', 'P2', 'T', 'G'}
        gumpy = 0,0
        # Se colocan los objetos aleatoriamente en el tablero (excepto en [1,1] y sin repetir coords)
        for obj in objetos:
            x, y = random.randint(0, 4), random.randint(0, 4)

            while (x, y) == (0, 0) or self.tablero[x][y] != ' ':
                x, y = random.randint(0, 4), random.randint(0, 4)
            if obj == 'G':
                gumpy = x,y
            elif obj == 'T':
                global tesoro
                tesoro = x,y
            self.tablero[x][y] = obj
        
        return gumpy
    

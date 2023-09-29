import random

#AGENTES
class Agentes: 

    def __init__(self, nombre, posicion_inicial):
        self.nombre = nombre
        self.posicion = posicion_inicial
        self.memoria_agente = [[0 for _ in range(5)] for _ in range(5)]
        self.historial = []
        self.objeto_encontrado = {'tesoro' : 'X', 'pozo1' : 'X', 'pozo2' : 'X', 'gumpy' : 'X', 'agI' : 'X'}

    def mostrar_stats(self, tablero, inicio, puntaje):
        #Con esto iremos mostrando las stats de cada agente
        print('Stats de:', self.nombre)
        
        if self.nombre == 'agI':
            print('Puntaje:', puntaje)

        if len(self.historial) == 0:
            print('Posicion:', self.posicion)
        else:
            posicion_anterior = self.historial[len(self.historial)-1] if len(self.historial) > 0 else self.posicion
            print('Posición anterior:', posicion_anterior)
        
        print('Posicion actual: ', self.posicion)

        self.historial.append(self.posicion) 

        self.sensores(tablero, inicio)

        print('\n')
        for fila in self.memoria_agente:
            for casilla in fila:
                print('\t', '[ ', casilla, ' ]' ,end='')
            print('\n')

        for key, valor in self.objeto_encontrado.items():
            print(key, ':', valor, end=' || ')

#SENSORES
    def sensores(self, tablero, inicio):
        if inicio:
            if self.nombre == 'gumpy':
                del self.objeto_encontrado['gumpy']
            elif self.nombre == 'agI':
                del self.objeto_encontrado['agI']
        
        for x in range(5):
            if int(self.posicion[0]) - x  >= -1 and int(self.posicion[0]) - x <= 1:
                 
                 for y in range(5):
                     if self.posicion[1] - y  >= -1 and self.posicion[1] - y <= 1:
                        if self.posicion[0] == x and self.posicion[1] == y:
                            continue
                        else:
                            #Checamos que se encuentra ahí
                            if tablero[x][y] != ' ': #ejecutamos el guardado en el diccionarios
                                self.memoria_agente[x][y] = self.encontrar_objeto(tablero[x][y], x, y)
                            else:
                                if self.memoria_agente[x][y] == 0:
                                    self.memoria_agente[x][y] = 1 
                                                   
    
    def encontrar_objeto(self, nombre_objeto, posx, posy):
        match nombre_objeto:
            case "A":
                if self.objeto_encontrado ['agI'] != 'X':
                    self.memoria_agente[self.objeto_encontrado['agI'][0]][self.objeto_encontrado['agI'][1]] = 1
                self.objeto_encontrado ['agI'] = posx,posy
                return 'agI'

            case "G":
                if self.objeto_encontrado ['gumpy'] != 'X':
                    self.memoria_agente[self.objeto_encontrado['gumpy'][0]][self.objeto_encontrado['gumpy'][1]] = 1
                self.objeto_encontrado['gumpy'] = posx,posy
                return 'gumpy'

            case "P1":
                self.objeto_encontrado['pozo1'] = posx,posy
                return 'pozo1'
            
            case "P2":
                self.objeto_encontrado['pozo2'] = posx,posy
                return 'pozo2'

            case "T":
                self.objeto_encontrado['tesoro'] = posx,posy
                return 'tesoro'

    # Función para mover el agente
    def mover_agente(self, tablero):
        inicial = 'X'
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Abajo, arriba, derecha, izquierda
        random.shuffle(directions)
        new_x = -1
        new_y = -1

        for dx, dy in directions:
            n_x, n_y = self.posicion[0] + dx, self.posicion[1] + dy
            #poner lo de gumpy y agi
            if is_valid(n_x, n_y):
                if self.nombre == 'gumpy':
                    inicial = 'G'
                    if tablero[n_x][n_y] == 'A':
                        new_x, new_y = n_x, n_y 
                        break
                    elif tablero[n_x][n_y] == ' ':
                        if self.memoria_agente[n_x][n_y] == 0:
                            new_x, new_y = n_x, n_y 
                            continue
                        elif self.memoria_agente[n_x][n_y] == 1:
                            new_x, new_y = n_x, n_y 
                            continue

                elif self.nombre == 'agI':
                    inicial = 'A'

                    tes = EO(self.memoria_agente,"tesoro")
                    if tes[0]==n_x|tes[1]==n_y:
                        new_x, new_y = tes[0], tes[1]
                        break

                    
                    
                    """if tablero[n_x][n_y] == 'T':
                        new_x, new_y = n_x, n_y 
                        break"""
                    if tablero[n_x][n_y] == ' ':
                        if self.memoria_agente[n_x][n_y] == 0:
                            new_x, new_y = n_x, n_y 
                            continue
                        elif self.memoria_agente[n_x][n_y] == 1:
                            new_x, new_y = n_x, n_y 
                            continue

        self.memoria_agente[self.posicion[0]][self.posicion[1]] = 1
        tablero[self.posicion[0]][self.posicion[1]] = ' '
        self.posicion = new_x, new_y
        tablero[self.posicion[0]][self.posicion[1]] = inicial 
        return tablero

def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def EO(matriz, objeto_buscado):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == objeto_buscado:
                print("encontrado")
                return fila, columna  # Devuelve la posición donde se encontró el objeto
    return None
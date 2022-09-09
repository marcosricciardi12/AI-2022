import random
import sys
import copy
import time

def pos_moviles(matriz):
    fichas_moviles = []
    for i in range(3):
        for j in range (3):
            if matriz[i][j] == 0:
                if i-1>=0:
                    fichas_moviles.append(matriz[i-1][j])
                if i+1<=2:    
                    fichas_moviles.append(matriz[i+1][j])
                if j-1>=0:    
                    fichas_moviles.append(matriz[i][j-1])
                if j+1<=2:    
                    fichas_moviles.append(matriz[i][j+1])
                return fichas_moviles, i, j
    

def mover(matriz, fichamovil, a, b):
    aux2 = True
    for k in range(3):
        for l in range (3):
            if matriz[k][l] == fichamovil:
                matriz[k][l] = 0
                matriz[a][b] = fichamovil
                return matriz


def mezclar(matriz):
    fichas_moviles, i, j = pos_moviles(matriz)
    r = random.randint(0, len(fichas_moviles)-1)
    # print("Piezas que se pueden mover del tablero anterior: " + str(fichas_moviles) + "\n")
    # print("Ficha a mover: " + str(fichas_moviles[r]) + "\n")
    matriz = mover(matriz, fichas_moviles[r], i, j)  
    return matriz                   


def search_random(t_mezc, t_ini):
    inicio = time.time()
    print("\nBusqueda aleatoria: ....")
    for line in t_mezc:
        print(line)
    count = 1
    solucion = False
    while not solucion:
        t_mezc = mezclar(t_mezc)
        if t_mezc == t_ini:
            solucion = True
        count = count + 1 
    fin = time.time()
    tiempo = fin-inicio
    print("Solucion random encontrada en %d movimietos!" % (count))
    print("Tiempo empleado para encontrar la solucion random: %f segundos" % (tiempo))
    for line in t_mezc:
        print(line)
    return t_mezc

def search_anchura(t_ini, arbol):
    inicio = time.time()
    way = True
    movimientos = []
    nivel = 0
    print("\n\nBusqueda por anchura, Buscando caminos...\n")
    while way:
        arbol_ant = copy.deepcopy(arbol)
        nivel = nivel + 1
        for nodo in arbol_ant:
            arbol.remove(nodo)
            fichas_moviles, a, b = pos_moviles(nodo[-1])
            for fichamovil in fichas_moviles:
                t_aux = copy.deepcopy(nodo[-1])
                t_aux = mover(t_aux, fichamovil, a, b)
                if t_aux == t_ini:
                    way = False
                    print("Victoria\n")
                isboard = False
                for board in movimientos:
                    if board == t_aux:
                        isboard = True
                        break
                if not isboard:
                    movimientos.append(t_aux)
                    nodo_aux = copy.deepcopy(nodo)
                    nodo_aux.append(t_aux)
                    arbol.append(nodo_aux)
                if not way:
                    break
            if not way:
                break
        if not way:
            break

    
    # print("Cant de movimientos repetidos: " + str(countrep))
    print("Camino de la solucion encontrada:\n")
    for line in arbol[-1]:
        print(line)
    print("\nEl camino de la solucion encontrada tiene %d pasos" % (len(arbol[-1])-1))
    print("El nivel actual del arbol (%d) tiene %d ramas" % (nivel, len(arbol)))
    print("Solucion en anchura encontrada en %d movimientos" % (len(movimientos)))
    fin = time.time()
    tiempo = fin - inicio
    print("Tiempo para encontrar solucion por anchura: %f segundos" % (tiempo))



                       



def main():
    arbol = [[]]

    t_vict = [  [1,2,3], 
                [4,5,6], 
                [7,8,0]]   

    t_init = [  [1,2,3], 
                [4,5,6], 
                [7,8,0]]

    print("Tablero inicial (condicion de victoria): ")
    for line in t_init:
        print(line)
    
    key = ''
    var = input("Ingrese la cantidad de veces a mezclar el tablero, si no ingresa nada podra mezclar manualmente: ")
    if var != '':
        for i in range(int(var)):
            mezclar(t_init)
    else:
        while key != 'c':
            key = input("\nEnter para mover fichas o c para mezclar por ultima vez: \n")
            mezclar(t_init)
            for i in range(3):
                for j in range(3):
                    if t_init[i][j] != 0:
                        print(" " + str(t_init[i][j]) + " ", end="")
                    else:
                        print("   ", end="")
                print("")
    t_aux = copy.deepcopy(t_init)
    arbol[0].append(t_aux)
    search_random(t_init, t_vict)    
    search_anchura(t_vict, arbol)
    


if __name__ == '__main__':
    main()
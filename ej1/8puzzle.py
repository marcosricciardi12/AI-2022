
import random
import sys
import copy
import time
sys.setrecursionlimit(10**6)



def mezclar(t_ini):
    fichas_moviles = []
    aux1 = False
    for i in range(3):
        for j in range (3):
            if t_ini[i][j] == 0:
                if i-1>=0:
                    fichas_moviles.append(t_ini[i-1][j])
                if i+1<=2:    
                    fichas_moviles.append(t_ini[i+1][j])
                if j-1>=0:    
                    fichas_moviles.append(t_ini[i][j-1])
                if j+1<=2:    
                    fichas_moviles.append(t_ini[i][j+1])
                r = random.randint(0, len(fichas_moviles)-1)
                print("Piezas que se pueden mover del tablero anterior: " + str(fichas_moviles) + "\n")
                print("Ficha a mover: " + str(fichas_moviles[r]) + "\n")
                aux2 = False
                for k in range(3):
                    for l in range (3):
                        if t_ini[k][l] == fichas_moviles[r]:
                            t_ini[k][l] = 0
                            t_ini[i][j] = fichas_moviles[r]
                            aux2 = True
                            break
                    if aux2:
                        break
                aux1 = True
                break
        if aux1:
            break
    return t_ini                      


def search_random(t_mezc, t_ini):
    fichas_moviles = []
    aux1 = False
    for i in range(3):
        for j in range (3):
            if t_mezc[i][j] == 0:
                if i-1>=0:
                    fichas_moviles.append(t_mezc[i-1][j])
                if i+1<=2:    
                    fichas_moviles.append(t_mezc[i+1][j])
                if j-1>=0:    
                    fichas_moviles.append(t_mezc[i][j-1])
                if j+1<=2:    
                    fichas_moviles.append(t_mezc[i][j+1])
                r = random.randint(0, len(fichas_moviles)-1)
                aux2 = False
                for k in range(3):
                    for l in range (3):
                        if t_mezc[k][l] == fichas_moviles[r]:
                            t_mezc[k][l] = 0
                            t_mezc[i][j] = fichas_moviles[r]
                            aux2 = True
                            break
                    if aux2:
                        break
                aux1 = True
                break
        if aux1:
            break
    if t_mezc == t_ini:
        print("Solucion encontrada!")
        for line in t_mezc:
            print(line)
        return False
    else:
        return True     

def search_anchura(t_ini, arbol, raiz):
    way = True
    print("Buscando caminos...")
    while way:
        arbol_ant = copy.deepcopy(arbol)
        for nodo in arbol_ant:
            # print(nodo)
            arbol.remove(nodo)
            fichas_moviles = []
            for i in range(3):
                for j in range (3):
                    if nodo[-1][i][j] == 0:
                        a = i
                        b = j
                        if i-1>=0:
                            fichas_moviles.append(nodo[-1][i-1][j])
                        if i+1<=2:    
                            fichas_moviles.append(nodo[-1][i+1][j])
                        if j-1>=0:    
                            fichas_moviles.append(nodo[-1][i][j-1])
                        if j+1<=2:    
                            fichas_moviles.append(nodo[-1][i][j+1])
            for mov in range(len(fichas_moviles)):
                t_aux = copy.deepcopy(nodo[-1])
                aux2 = True
                for k in range(3):
                    for l in range (3):
                        if t_aux[k][l] == fichas_moviles[mov] and aux2:
                            t_aux[k][l] = 0
                            t_aux[a][b] = fichas_moviles[mov]
                            aux2 = False
                if t_aux == t_ini:
                    way = False
                    print("Victoria")
                tablerois = False
                for nodo2 in arbol_ant:
                    if t_aux in nodo2:
                        tablerois = True
                        break
                if not tablerois:
                    nodo_aux = copy.deepcopy(nodo)
                    nodo_aux.append(t_aux)
                    arbol.append(nodo_aux)
                if not way:
                    break
            if not way:
                break
        if not way:
            break

    
    
    print(arbol[-1])   
    print(len(arbol))
    print(len(arbol[-1]))



                       



def main():
    arbol = [[]]
    raiz = 0
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
    while key != 'c':
        key = input("\nEnter para mover fichas o c para mezclar por ultima vez: \n")
        t_mezclado = mezclar(t_init)
        for i in range(3):
            for j in range(3):
                if t_mezclado[i][j] != 0:
                    print(" " + str(t_mezclado[i][j]) + " ", end="")
                else:
                    print("   ", end="")
            print("")
    count = 0
    print("\nBusqueda aleatoria: ....")
    t_aux = copy.deepcopy(t_mezclado)
    arbol[raiz].append(t_aux)
    while search_random(t_mezclado, t_vict):
        count = count + 1
    print("\nSolucion encontrada en " + str(count) + " movimientos!")
    inicio = time.time()
    search_anchura(t_vict, arbol, raiz)
    fin = time.time()
    tiempo = fin - inicio
    print("Tiempo para encontrar solucion por anchura: " + str(tiempo))


if __name__ == '__main__':
    main()
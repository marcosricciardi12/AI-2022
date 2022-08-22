# [   [00,01,02]  
#     [10,11,12]
#     [20,21,22]]
import random
import sys 
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
    fichas_moviles = []
    raiz = raiz + 1
    print(arbol)
    arbol.append(arbol[raiz-1])
    for i in range(3):
        for j in range (3):
            if arbol[raiz][-1][i][j] == 0:
                a = i
                b = j
                if i-1>=0:
                    fichas_moviles.append(arbol[raiz][-1][i-1][j])
                if i+1<=2:    
                    fichas_moviles.append(arbol[raiz][-1][i+1][j])
                if j-1>=0:    
                    fichas_moviles.append(arbol[raiz][-1][i][j-1])
                if j+1<=2:    
                    fichas_moviles.append(arbol[raiz][-1][i][j+1])            
    for p in range(len(fichas_moviles)):
        t_aux = arbol[raiz][-1]
        aux1 = False
        for k in range(3):
            for l in range (3):
                if t_aux[k][l] == fichas_moviles[p]:
                    t_aux[k][l] = 0
                    t_aux[a][b] = fichas_moviles[p]
                    aux1 = True
                    if t_aux == t_ini:
                        print("Camino encontrado!")
                        arbol[raiz].append(t_aux)
                    else:
                        if t_aux not in arbol[raiz]:
                            print("Agregando camino")
                            arbol[raiz].append(t_aux)
                            for line in t_aux:
                                print(line)
                            print("")
                            search_anchura(t_ini, arbol, raiz)
                    break
            if aux1:
                break
                       



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
    t_aux = t_mezclado
    arbol[raiz].append(t_aux)
    print(arbol)
    while search_random(t_mezclado, t_vict):
        count = count + 1
    print("\nSolucion encontrada en " + str(count) + " movimientos!")
    print(arbol)
    # search_anchura(t_vict, arbol, raiz)




if __name__ == '__main__':
    main()
from perceptron import Perceptron
from math import fabs

def corregir_pesos(list_salida, pesos, salida_deseada, list_perceptrones):
    LR = 0.1
    for p_sal in list_salida:
        error = float(salida_deseada) - float(p_sal.salida)
        if fabs(error) >  0.1:
            delta = p_sal.salida*(1-p_sal.salida)*error
            for p in list_perceptrones:
                # print(pesos)
                for i in range(len(p.entradas)):
                    dw = LR * p.entradas[i] * delta
                    pesos[i] = p.pesos[i] + dw
        else:
            return False
    return True


def main():

    cant_entrada = 2 #tantos perceptrones como cantidad de entradas
    cant_oculta = 3
    cant_salida = 1
    pesos = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1, -0.23, -0.79, 0.56, 0.6, -0.6, 0.22, -0.22, -0.55, 0.31 ,-0.32]
    list_entrada = []
    list_oculta = []
    list_salida = []
    list_perceptrones = []

    tabla_xor = [   [1,0,0,0],
                    [1,0,1,1],
                    [1,1,0,1],
                    [1,1,1,0]]
    pos_peso = 0
    for p in range(cant_entrada):
        list_entrada.append(Perceptron())
        list_entrada[p].entradas = [float for x in range(cant_entrada+1)]
        for i in range(cant_entrada + 1):
            list_entrada[p].pesos.append(pesos[pos_peso])
            pos_peso = pos_peso + 1
    for p in range(cant_oculta):
        list_oculta.append(Perceptron())
        list_oculta[p].entradas = [float for x in range(cant_entrada+1)]
        for i in range(cant_entrada + 1):
            list_oculta[p].pesos.append(pesos[pos_peso])
            pos_peso = pos_peso + 1
    for p in range(cant_salida):
        list_salida.append(Perceptron())
        list_salida[p].entradas = [float for x in range(cant_oculta+1)]
        for i in range(cant_oculta + 1):
            list_salida[p].pesos.append(pesos[pos_peso])
            pos_peso = pos_peso + 1

    list_perceptrones = list_entrada + list_oculta + list_salida

    corregir = True
    while True:
        print(pesos)
        for linea in tabla_xor:
            input()
            for p_ent in list_entrada:
                for i in range(len(linea)-1):
                    p_ent.entradas[i] = linea[i]
                p_ent.calc_salida()
                print("\nPerceptron entrada:")
                p_ent.mostrar_val()

            for p_ocu in list_oculta:
                for i in range(len(list_entrada)+1):
                    if i == 0:
                        p_ocu.entradas[i] = 1
                    else:
                        p_ocu.entradas[i] = float(list_entrada[i-1].salida)
                p_ocu.calc_salida()
                print("\nPerceptron oculto:")
                p_ocu.mostrar_val()

            for p_sal in list_salida:
                for i in range(len(list_oculta)+1):
                    if i == 0:
                        p_sal.entradas[i] = 1
                    else:
                        p_sal.entradas[i] = float(list_oculta[i-1].salida)
                p_sal.calc_salida()
                print("\nPerceptron salida:")
                p_sal.mostrar_val()
              
            corregir = corregir_pesos(list_salida, pesos, linea[-1], list_perceptrones)

            




    




if __name__ == '__main__':
    main()
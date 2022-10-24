from perceptron import Perceptron
from math import fabs
import matplotlib.pyplot as plt
import copy
import random
from read_images import read_images

def graph(lista_datos, nombre):
    plt.figure(figsize=(10,7))
    x = []
    x = range(len(lista_datos))
    for i in range(len(lista_datos[0])):
        y = []
        for j in range(len(lista_datos)):
            y.append(lista_datos[j][i])
        plt.plot(x, y, label = "W%d" %(i))
    plt.title(nombre)
    plt.legend()
    plt.savefig(nombre + ".png")
    plt.show()
    plt.close()

def corregir_pesos(list_salida, pesos, salida_deseada, list_perceptrones, historico_pesos, historico_error):
    LR = 0.5
    pos_peso = 0
    
    for p_sal in list_salida:
        # print(salida_deseada, p_sal.salida)
        error = float(salida_deseada) - float(p_sal.salida)
        # print("Error: %f" % error)
        delta_fin = p_sal.salida*(1-p_sal.salida)*error
        
        if fabs(error) >  0.1:
            
            for p in list_perceptrones:
                # print(pesos)
                
                p.pesos.clear()
                for entrada in p.entradas:
                    # print(p.salida)
                    delta = p.salida*(1-p.salida)*delta_fin
                    # print("Delta: %f" % (delta))
                    dw = LR * entrada * delta
                    # print("dw: %f" % (dw))
                    pesos[pos_peso] = pesos[pos_peso] + dw
                    p.pesos.append(pesos[pos_peso])
                    pos_peso = pos_peso + 1


            # historico_pesos.append(copy.deepcopy(pesos))

        
        else:
            return False
    return True

def main():

    cant_entrada = 0 #tantos perceptrones como cantidad de entradas
    cant_oculta = 10
    cant_salida = 1
    pesos = []
    list_entrada = []
    list_oculta = []
    list_salida = []
    list_perceptrones = []
    historico_pesos = []
    historico_error = []
    input("Presione enter para comenzar")
    
    historico_pesos.append(copy.deepcopy(pesos))
    tabla_imagenes = read_images()
    entradas = len(tabla_imagenes[0])-2
    cant_entrada = 0
    cant_pesos = (cant_entrada*cant_entrada+cant_entrada) + (entradas*cant_oculta+cant_oculta) + (cant_oculta*cant_salida+cant_salida)
    
    for i in range(cant_pesos):
        pesos.append(random.uniform(-0.01,0.01))
    pos_peso = 0

    for p in range(cant_entrada):
        list_entrada.append(Perceptron())
        list_entrada[p].entradas = [float for x in range(cant_entrada+1)]
        for i in range(cant_entrada + 1):
            list_entrada[p].pesos.append(pesos[pos_peso])
            pos_peso = pos_peso + 1

    for p in range(cant_oculta):
        list_oculta.append(Perceptron())
        list_oculta[p].entradas = [float for x in range(entradas+1)]
        for i in range(entradas + 1):
            list_oculta[p].pesos.append(pesos[pos_peso])
            pos_peso = pos_peso + 1

    for p in range(cant_salida):
        list_salida.append(Perceptron())
        list_salida[p].entradas = [float for x in range(cant_oculta+1)]
        for i in range(cant_oculta + 1):
            list_salida[p].pesos.append(pesos[pos_peso])
            pos_peso = pos_peso + 1

    list_perceptrones = list_entrada + list_oculta + list_salida
    print("\nPesos iniciales:\n ")
    print(cant_pesos)
    # for i in range(len(pesos)):
    #     print("\tw%d: %f" % (i, pesos[i]))
    corregir = True
    count = 0
    while corregir:
        count += 1
        print("Cantidad de iteraciones: %d" % (count))
        # input("Enter para continuar...")
        error = []
        for linea in tabla_imagenes:
            # input("Enter para continuar...")
            for p_ent in list_entrada:
                for i in range(len(linea)-1):
                    p_ent.entradas[i] = linea[i]
                p_ent.calc_salida()
                # print("\nPerceptron entrada:")
                # p_ent.mostrar_val()

            if  cant_entrada == 0:
                for p_ocu in list_oculta:
                    for i in range(len(linea)-1):
                        p_ocu.entradas[i] = linea[i]
                    p_ocu.calc_salida()
                    # print("\nPerceptron Oculto:")
                    # p_ocu.mostrar_val()
            else:
                 for p_ocu in list_oculta:
                    for i in range(len(list_entrada)+1):
                        if i == 0:
                            p_ocu.entradas[i] = 1
                        else:
                            p_ocu.entradas[i] = float(list_entrada[i-1].salida)
                    p_ocu.calc_salida()
                    # print("\nPerceptron oculto:")
                    # p_ocu.mostrar_val()

            for p_sal in list_salida:
                for i in range(len(list_oculta)+1):
                    if i == 0:
                        p_sal.entradas[i] = 1
                    else:
                        p_sal.entradas[i] = float(list_oculta[i-1].salida)
                p_sal.calc_salida()
                # print("\nPerceptron salida:")
                # print(linea)
                # p_sal.mostrar_val()
                error.append((linea[-1]-p_sal.salida))  
            corregir = corregir_pesos(list_salida, pesos, linea[-1], list_perceptrones, historico_pesos, historico_error)
            # print("\nPesos corregidos: ")
            # for i in range(len(pesos)):
            #     print("\tw%d: %f" % (i, pesos[i]))
        # historico_error.append(error)

    print("Cantidad de iteraciones: %d" % (count))
    # graph(historico_pesos, "Pesos")
    # graph(historico_error, "Errores")
            




    




if __name__ == '__main__':
    main()

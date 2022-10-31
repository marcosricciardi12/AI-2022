from perceptron import Perceptron
import matplotlib.pyplot as plt
import copy
from read_images import read_images
from read_pesos import read_pesos
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


def main():

    cant_entrada = 0 #tantos perceptrones como cantidad de entradas
    cant_oculta = 50
    cant_salida = 1
    pesos = []
    list_entrada = []
    list_oculta = []
    list_salida = []

    input("Presione enter para comenzar")
    
    tabla_imagenes = read_images()
    entradas = len(tabla_imagenes[0])-2
    print("Cant de entradas: %d" % entradas)
    cant_entrada = 0
    
    pesos = read_pesos()
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


    for linea in tabla_imagenes:

            for p_ent in list_entrada:
                p_ent.entradas = copy.deepcopy(linea[0:-1])
                p_ent.calc_salida()
                # print("\nPerceptron entrada:")
                # p_ent.mostrar_val()

            if  cant_entrada == 0:
                for p_ocu in list_oculta:
                    p_ocu.entradas = copy.deepcopy(linea[0:-1])
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
                print("\n Salida Deseada: %f    Perceptron salida: %f" % (linea[-1], p_sal.salida))
                # print(linea)
                # p_sal.mostrar_val()


            




    




if __name__ == '__main__':
    main()

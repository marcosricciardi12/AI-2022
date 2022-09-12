from cProfile import label
import random
from math import e
from math import fabs
import matplotlib.pyplot as plt

def main():         
                #   e1 e2 SD
    tabla_or = [   [0,0,0],
                    [0,1,1],
                    [1,0,1],
                    [1,1,1]]
    LR = 0.1
    w0 = random.uniform(-1,1)
    w1 = random.uniform(-1,1)
    w2 = random.uniform(-1,1)
    w0 = 0.9
    w1 = 0.66
    w2 = -0.2
    SR = []
    graph_error = [[] for i in range(len(tabla_or))]
    peso0 = []
    peso1 = []
    peso2 = []
    pos_x = []
    error = 1
    print("Perceptron simple compuerta OR")
    print("\nPesos iniciales: \nw0 = %f \nw1 = %f \nw2 = %f "%(w0, w1, w2))
    input("\nPresione enter para continuar. Error menor a 0.0001")
    count = 0
    a=0
    while fabs(error) > 0.0001:
        pos_x.append(a)
        for linea in tabla_or:
            # input()
            x = 1*w0 + linea[0]*w1 + linea[1]*w2
            y = 1/(1+e**(-x))
            error = linea[2] - y
            # print(error)
            graph_error[count%4].append(error)
            delta = y*(1-y)*error
            dw0 = LR * 1 * delta
            w0 = w0 + dw0
            dw1 = LR * linea[0] * delta
            w1 = w1 + dw1
            dw2 = LR * linea[1] * delta
            w2 = w2 + dw2
            # print("w0 = %f \nw1 = %f \nw2 = %f "%(w0, w1, w2))
            peso0.append(w0)
            peso1.append(w1)
            peso2.append(w2)
            count = count + 1
        a = a+1
        # if a == 1000:
        #     break
    print("\nResultados finales")
    print("Cantidad de iteraciones: %d" %(a))
    print("w0 = %f \nw1 = %f \nw2 = %f "%(w0, w1, w2))
    er = 0
    plt.figure(figsize=(10,7))
    for err in graph_error:
        er += 1
        plt.plot(pos_x, err,markersize=5,label = "error de %d" %(er))
    plt.title("Errores_or")
    plt.legend()
    plt.savefig("errores_or.png")
    plt.show()
    plt.close()
    plt.figure(figsize=(10,7))
    plt.plot(range(count), peso0, label = "W0")
    plt.plot(range(count), peso1,label = "W1")
    plt.plot(range(count), peso2, label = "W2")
    plt.title("Pesos_or")
    plt.legend()
    plt.savefig("pesos_or.png")
    plt.show()
    plt.close()
    
    


    

if __name__ == '__main__':
    main()
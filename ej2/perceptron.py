import random
from math import e
from math import fabs
import matplotlib.pyplot as plt

def main():         
                #   e1 e2 SD
    tabla_and = [   [0,0,0],
                    [0,1,0],
                    [1,0,0],
                    [1,1,1]]
    LR = 0.1
    # w0 = random.uniform(-1,1)
    # w1 = random.uniform(-1,1)
    # w2 = random.uniform(-1,1)
    w0 = 0.9
    w1 = 0.66
    w2 = -0.2
    SR = []
    graph_error = [[] for i in range(len(tabla_and))]
    pos_x = []
    error = 1
    print(w0)
    print(w1)  
    print(w2)
    input()
    count = 0
    a=0
    while fabs(error) > 0.1:
        pos_x.append(a)
        for linea in tabla_and:
            # input()
            x = 1*w0 + linea[0]*w1 + linea[1]*w2
            y = 1/(1+e**(-x))
            print("salida real: %f" % (y))
            error = linea[2] - y
            print("Error: %f" % (error))
            # print(error)
            graph_error[count%4].append(error)
            if fabs(error) >  0.1:
                delta = y*(1-y)*error
                dw0 = LR * 1 * delta
                w0 = w0 + dw0
                dw1 = LR * linea[0] * delta
                w1 = w1 + dw1
                dw2 = LR * linea[1] * delta
                w2 = w2 + dw2
                # print("w0 = %f \nw1 = %f \nw2 = %f "%(w0, w1, w2))
            count = count + 1
        a = a+1
    print("Cantidad de iteraciones: %d" %(count))
    print("w0 = %f \nw1 = %f \nw2 = %f "%(w0, w1, w2))
    plt.figure(figsize=(10,7))
    for err in graph_error:
        plt.plot(pos_x, err,color='orange',markersize=5)
    plt.show()
    plt.close()
    
    


    

if __name__ == '__main__':
    main()

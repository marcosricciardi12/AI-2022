from math import e
from math import fabs

class Perceptron:
    def __init__(self):
        self.entradas = []
        self.pesos = []
        self.salida = float
    
    def calc_salida(self):
            x = float(0)
            # print(self.entradas)
            # print(self.pesos)
            for i in range(len(self.entradas)):
                x = x + (self.entradas[i] * self.pesos[i])
            self.salida = float(1/(1+e**(-x)))

    def mostrar_val(self):
        for i in range(len(self.entradas)):
            print("Entrada: %f . Peso: %f" % (self.entradas[i], self.pesos[i]))
        print("Salida: %f" % (self.salida))
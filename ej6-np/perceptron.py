from math import e
from math import fabs
import numpy as np

class Perceptron:
    def __init__(self):
        self.entradas = np.empty(0, dtype=float)
        self.pesos = np.empty(0, dtype=float)
        self.salida = float
    
    def calc_salida(self):
        print(self.entradas[-1])
        print(self.pesos[-1])
        x = float(np.sum(np.multiply(self.entradas, self.entradas)))
        print(x)
        self.salida = float(1/(1+e**(-x)))

    def mostrar_val(self):
        for i in range(len(self.entradas)):
            print("Entrada: %f . Peso: %f" % (self.entradas[i], self.pesos[i]))
        print("Salida: %f" % (self.salida))
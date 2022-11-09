
def read_pesos():
    list_pesos = []
    with open('pesos.txt', 'r') as pesos:
        for line in pesos:
            list_pesos.append(float(line))
    return (list_pesos)
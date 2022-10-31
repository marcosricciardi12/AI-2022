
def read_pesos():
    list_pesos = []
    with open('pesos.txt', 'r') as pesos:
        for line in pesos:
            list_pesos.append(float(line))
    print(list_pesos[0:10])
    return (list_pesos)
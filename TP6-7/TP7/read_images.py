import cv2
import copy
import os
def read_images():
    print("Cargando imagenes, por favor espere")
    image_px = []
    aux = []
    persona = True
    for i in range(6):
        img = cv2.imread("prueba/" + str(i) + ".jpg", 0)
        aux.clear()
        aux.append(1) #Agrego Vias a la entrada
        for j in range(len(img)):
            for k in range(len(img[j])):
                px = img[j][k]
                exceso = 0
                for l in range(8):
                    if l < 8-len(bin(px)[2:]):
                        aux.append(0)
                        exceso = exceso + 1
                    else:
                        aux.append(int(bin(px)[2+l-exceso]))

        # Agrego salida esperada para persona A o B
        if persona:
            aux.append(int(0))
            persona = False
        else:
            aux.append(1)
            persona = True
            
        image_px.append(copy.deepcopy(aux))
    os.system ("clear")
    print("Imagenes procesadas.")
    return image_px


    

import cv2
import copy
import os
def read_images():
    print("Cargando imagenes, por favor espere")
    image_px = []
    aux = []
    persona = True
    for i in range(10):
        img = cv2.imread("leer/" + str(i) + ".jpg", 0)
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
        aux.clear()
        aux.append(int(1)) #Agrego Vias a la entrada
        for j in range(len(img)):
            for k in range(len(img[j])):
                px = img[j][k]
                if px == 0:
                    aux.append(int(0))
                else:
                    aux.append(int(1))
                

        # Agrego salida esperada para persona A o B
        if persona:
            aux.append(int(0))
            persona = False
        else:
            aux.append(1)
            persona = True
        image_px.append(copy.deepcopy(aux))
    # os.system ("clear")
    print("Imagenes procesadas.")
    return image_px


    

import cv2
import copy

def read_images():
    image_px = []
    aux = []
    persona = True
    for i in range(10):
        img = cv2.imread("leer/" + str(i) + ".jpg", cv2.COLOR_RGB2GRAY)
        aux.clear()
        aux.append(1) #Agrego Vias a la entrada
        for j in range(len(img)):
            for k in range(len(img[0])):
                px = img[j][k][0]
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
    print(len(image_px[0]))
    return image_px

read_images()

    

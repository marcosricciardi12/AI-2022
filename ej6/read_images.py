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
                aux.append(px/255)

        # Agrego salida esperada para persona A o B
        if persona:
            aux.append(int(0))
            persona = False
        else:
            aux.append(1)
            persona = True
            
        image_px.append(copy.deepcopy(aux))

    return image_px

read_images()    

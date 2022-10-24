import cv2
import copy

def read_images():
    image_px = []
    aux = []
    for i in range(10):
        print(i)
        img = cv2.imread("leer/" + str(i) + ".jpg", cv2.COLOR_RGB2GRAY)
        aux.clear()
        for j in range(len(img)):
            for k in range(len(img[0])):
                px = img[j][k][0]
                aux.append(px)
        image_px.append(copy.deepcopy(aux))

    print(image_px[0][0], image_px[0][1])
    print(len(image_px[0]))

read_images()
    

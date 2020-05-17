import numpy as np
import cv2

img = cv2.imread('lena.jpg')
layer = img.copy()
gp =[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

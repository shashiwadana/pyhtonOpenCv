import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=2)
erosion = cv2.erode(mask,kernel,iterations=1) #erode the boundary of foreground objects
opening =cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)#erosion+dialation
closing =cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)#dialation+erosion

titles = ['image','mask','dialation','erosion','opening','closing']
images = [img,mask,dilation,erosion,opening,closing]

for i in range(6):
    plt.subplot( 2, 3, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


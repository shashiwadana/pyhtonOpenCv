import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=2)
erosion = cv2.erode(mask,kernel,iterations=1) #erode the boundary of foreground objects

titles = ['image','mask','dialation','erosion']
images = [img,mask,dilation,erosion]

for i in range(4):
    plt.subplot( 2, 2, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


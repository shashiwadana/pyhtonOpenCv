import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=2)

titles = ['image','mask','dialation']
images = [img,mask,dilation]

for i in range(3):
    plt.subplot( 1, 3, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


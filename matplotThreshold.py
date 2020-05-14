import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #compare with thresh and assign 0 or 1
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) #upto the threshold values of pixels won't be changed,after thresh pixel value remains same
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)#pixel value<thresh assign it to 0
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['original','binary','binInvert','trunc','toZero','toZeroInvert']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot( 2, 3, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


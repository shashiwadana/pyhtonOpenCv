import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25 #homogeneous filtering
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0) #gaussian blur is to remove high frequency noise


titles = ['image','2D','blur','gblur']
images = [img,dst,blur,gblur]

for i in range(4):
    plt.subplot( 2, 2, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


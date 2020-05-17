import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap)) #get absolute value and transform to unsigned 8bit int
sobleX= cv2.Sobel(img,cv2.CV_64F,1,0) #order od derivative x
sobleY= cv2.Sobel(img,cv2.CV_64F,0,1)

sobleX =np.uint8(np.absolute(sobleX))
sobleY =np.uint8(np.absolute(sobleY))
titles = ['image','lap','sobX','sobY']
images = [img,lap,sobleX,sobleY]

for i in range(4):
    plt.subplot( 2, 2, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


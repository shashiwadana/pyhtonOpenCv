import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap)) #get absolute value and transform to unsigned 8bit int


titles = ['image','lap']
images = [img,lap]

for i in range(2):
    plt.subplot( 1, 2, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


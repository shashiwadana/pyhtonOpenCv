import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi_face.jpg',0)
w, h=template.shape[::-1]
res = cv2.matchTemplate(gray_image,template,cv2.TM_CCOEFF_NORMED)
print(res)
threshold = 0.9
loc= np.where(res>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

img1 = np.zeros((512,512,3), np.uint8)
cv2.rectangle(img1, (200,0), (300,100), (255, 255, 255), -1)
img2 = cv2.imread('lena.jpg')

#bitAnd = cv2.bitwise_and(img1, img2)
#bitOr = cv2.bitwise_or(img1,img2)
#bitxOr = cv2.bitwise_xor(img1,img2)
bitnot = cv2.bitwise_not(img2)


#cv2.imshow('image',img1)
#cv2.imshow('image',img2)
cv2.imshow('and',bitnot)
cv2.waitKey(0)
cv2.destroyAllWindows()

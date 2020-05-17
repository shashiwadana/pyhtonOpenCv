import numpy as np
import cv2

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
apple_orange =np.hstack((apple[:,:256],orange[:,256:]))

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('Apple-orange',apple_orange)
cv2.waitKey(0)
cv2.destroyAllWindows()

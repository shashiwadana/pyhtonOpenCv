import numpy as np
import cv2

img = cv2.imread('gradient.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #compare with thresh and assign 0 or 1

cv2.imshow('image',img)
cv2.imshow('threshold',th1)

cv2.waitKey(0)
cv2.destroyAllWindows()

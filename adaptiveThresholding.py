import numpy as np
import cv2

img = cv2.imread('sudoku.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) #take the mean of neighbours

cv2.imshow('image',img)
cv2.imshow('threshold 2',th2)
cv2.waitKey(0)
cv2.destroyAllWindows()

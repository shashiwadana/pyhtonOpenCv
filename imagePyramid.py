import numpy as np
import cv2

img = cv2.imread('lena.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr = cv2.pyrUp(lr2)

cv2.imshow('Original image',img)
cv2.imshow('lower  res image',lr1)
cv2.imshow('lower  res2 image',lr2)
cv2.imshow('higher  res2 image',hr)
cv2.waitKey(0)
cv2.destroyAllWindows()

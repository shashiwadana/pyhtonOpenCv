import  numpy as np
import cv2

img = cv2.imread('messi5.jpg')
print(img.shape) #returns a tuple of no of rows columns and channels
print(img.size) #returns total num of pixels accessed
print(img.dtype) #image data type
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390] #range of interest
img[273:333, 100:160 ] = ball #assign the ball to this coordinate


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

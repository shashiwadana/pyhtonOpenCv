import cv2

img = cv2.imread('lena.jpg',1)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)  #arguments are image,start coordinate as a tuple,end ,color in BGR and thicknes
img = cv2.arrowedLine(img, (0,255), (255,255), (0,0,255), 5)
img = cv2.rectangle(img, (384,0), (450,125), (0,255,0), 5)
img = cv2.circle(img, (300,63), 63, (0,255,255), -1) #-1 to fill the shape

font=cv2.FONT_ITALIC
img = cv2.putText(img, 'OpenCV', (10,100), font, 4, (0,0,0), 10, cv2.LINE_AA)

cv2.imshow('lena',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

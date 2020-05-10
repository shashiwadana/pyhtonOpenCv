import cv2
img = cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF

if k == 27:                  #if user pressed escape key
    cv2.destroyAllWindows()
elif k == ord('s'):          #if user pressed 's' key
    cv2.imwrite('lena_copied.jpg', img)
    cv2.destroyAllWindows()
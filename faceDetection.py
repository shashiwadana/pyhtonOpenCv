import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('messi5.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grey, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)


cv2.imshow("image",img)
cv2.waitKey()
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("/home/pi/Desktop/day03/haarcascade_frontalface_default.xml")

img = cv2.imread('/home/pi/Desktop/IoT_Group.jpg')
resizeImg = cv2.resize(img, (640, 480))
gray = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.2, 5)

count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(img, str(count), (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    count = count + 1

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
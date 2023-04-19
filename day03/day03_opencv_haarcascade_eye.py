import cv2
import numpy as np

eye_cascade = cv2.CascadeClassifier("/home/pi/Desktop/day03/haarcascade_eye.xml")

img = cv2.imread("/home/pi/Desktop/pngegg.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(gray, 1.2, 5)

for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
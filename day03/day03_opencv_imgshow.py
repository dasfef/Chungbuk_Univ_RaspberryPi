import cv2
import numpy as np

img = cv2.imread('/home/pi/Desktop/test2.jpg', cv2.IMREAD_COLOR)
R_img, G_img, B_img = cv2.split(img)
zeroImg = np.zeros((img.shape[0], img.shape[1]), dtype = 'uint8')
mergeImg = cv2.merge([B_img, zeroImg, R_img])

cv2.imshow('photo', mergeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
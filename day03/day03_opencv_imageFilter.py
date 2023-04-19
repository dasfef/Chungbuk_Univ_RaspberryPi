import cv2
import numpy as np

img = cv2.imread('/home/pi/Desktop/Fresh.jpg')
img2 = cv2.imread('/home/pi/Desktop/Fresh.jpg')

# -- dilate --
kernel = np.ones((5, 5), np.uint8)
filteredImg = cv2.dilate(img, kernel, iterations = 1)

# -- erode --
# kernel = np.ones((5, 5), np.uint8)
# filteredImg = cv2.erode(img, kernel, iterations = 1)

# -- embossing --
# Filter = np.array([[1, 0, 0], [0, 0, 0], [0, 0, -1]])
# filteredImg = cv2.filter2D(img, -1, Filter)

# -- sharpeningFilter --
# sharpeningFilter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# sharpeningFilter2 = np.array([[-1, -1, -1, -1, -1], [-1, 2, 2, 2, -1], [-1, 2, 9, 2, -1], [-1, 2, 2, 2, -1], [-1, -1, -1, -1, -1]]) / 9.0
# filteredImg = cv2.filter2D(img, -1, sharpeningFilter2)

# -- bilateralFilter --
# filteredImg = cv2.bilateralFilter(img, 5, 75, 75)

# -- GaussianBlur --
# filteredImg = cv2.GaussianBlur(img,(33,33), 0)

cv2.imshow('Image_origin', img2)
cv2.imshow('Image', filteredImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ah noogoo ya nae code gundrinunnom
# sry
# sil
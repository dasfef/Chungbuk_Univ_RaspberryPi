import cv2

img = cv2.imread('/home/pi/Desktop/test2.jpg')
img2 = cv2.imread('/home/pi/Desktop/test.jpg')

# -- cv bitwise_and --
maskImg = cv2.imread('/home/pi/Desktop/mask.png')
masked = cv2.bitwise_xor(img2, maskImg) # and, or, xor

# -- cv absdiff --
# mathImg = cv2.bitwise_not(cv2.absdiff(img2, img))

# -- cv color --
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -- cv multiply --
# mathImg = cv2.multiply(gray, 2)

# -- cv add --
# mathImg = cv2.add(gray, -100)

# -- thresh hold --
# ret, threshHoldImage = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY) 

cv2.imshow('PHOTO', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
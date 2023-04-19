import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# -- putText --
img = cv2.putText(img, "Choi Yeon Woong", (80, 300), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10)

# -- polylines --
# pts = np.array([[100, 20], [200, 300], [400, 300], [500, 100]], np.int32)
# pst = pts.reshape((-1, 1, 2))
# img = cv2.polylines(img, [pts], True, (0, 255, 255))

# -- ellipse --
# img = cv2.ellipse(img, (320, 240), (100, 50), 0, 0, 270, 255, -1)

# -- circle --
# img = cv2.circle(img, (320, 240), 100, (0, 255, 0), -1) # -1 == fill the circle

# -- rectangle --
# img = cv2.rectangle(img, (10, 10), (629, 469), (0, 0, 255), 2)

# -- line --
# img = cv2.line(img, (0, 0), (639, 479), (255, 255, 0), 5)

cv2.imshow('draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
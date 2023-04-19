import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("/home/pi/Desktop/day03/haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("/home/pi/Desktop/day03/haarcascade_smile.xml")

video = "/home/pi/Desktop/people2.mp4"
cap = cv2.VideoCapture(video)



if not cap.isOpened():
    print("Video open failed")
    sys.exit()
    
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    count = 0
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, str(count), (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        count = count + 1
    cv2.imshow("VIDEO", frame)
    
    if cv2.waitKey(20) == 27:
        break
cap.release()
cv2.destroyAllWindows()
# 
# if cap.isOpened() :
#     ret, img = cap.read()
#     if ret:
#         cv2.imshow("Vidoe", img)
#         
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         
#         if ret :
#             for (x, y, w, h) in faces:
#                 img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
#                 roi_gray = gray[y:y+h, x:x+w]
#                 roi_color = img[y:y+h, x:x+w]
#                 smile = smile_cascade.detectMultiScale(roi_gray)
#                 for(ex, ey, ew, eh) in smile:
#                     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#             cv2.imshow("video", img)
#             cv2.waitKey(25)
#         else:
#             break
# else:
#     print("Can't open the video")
# cap.release()
# cv2.destroyAllWindows()

# img = cv2.imread("/home/pi/Desktop/people.mp4")



        
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2

# if something goes wrong, change Camera Index 
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) > 0:
        break;
    
cap.release()

img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

cv2.destroyWindow("Camera")
cv2.imshow("Image", img)

key = cv2.waitKey(0)

cv2.destroyWindow("Image")

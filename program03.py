import cv2

# if something goes wrong, change Camera Index 
cap = cv2.VideoCapture(0) 

while True:
    ret,frame = cap.read()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) > 0:
        break
    
cap.release()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(frame, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

cv2.destroyWindow("Camera")
cv2.imshow("Image", frame)

key = cv2.waitKey(0)

cv2.destroyWindow("Image")

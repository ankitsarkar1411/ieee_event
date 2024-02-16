import cv2
cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=cascade.detectMultiScale(gray,1.03,6)
    for x,y,w,h in face:
        frame=cv2.rectangle(frame,(x,y),(x,y,w,h),(255,0,0),2)
    cv2.imshow("normal video",frame)
    if cv2.waitKey(1) == 13:
       break
cap.release()
cv2.destroyAllWindows   
import cv2
fire_cascade=cv2.CascadeClassifier("fire_detection.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire= fire_cascade.detectMultiScale(gray,1.2,5)
    for x,y,w,h in fire:
        cv2.rectangle(frame,(x+20,y+20),(x+w-20,y+h-20),(0,255,0),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        print("Fire is detected")
    cv2.imshow("frame",frame)    
    if cv2.waitKey==13:
       break
cap.release()
cv2.destroyAllWindows()    
import cv2

cap = cv2.VideoCapture(0)

## added
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
## ended

while(True):
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret==False:
        continue
    ## add
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5) 
    print(faces)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    ## end
    
    cv2.imshow("Video Frame",frame)
    # cv2.imshow("Black White",gray_frame)
    # Wait For user input
    key_pressed = cv2.waitKey(1) & 0xFF
    
    if(key_pressed == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
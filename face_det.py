#!/usr/bin/python3
import cv2
casclf=cv2.CascadeClassifier('face.xml')  # download xml file  at https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml and download with wget and mv file in face.xml for  easy to write 

 
#loading face 
cap=cv2.VideoCapture(0)
while cap.isOpened() :
    status,frame=cap.read()

    face=casclf.detectMultiScale(frame,1.13,5)

    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
        facedata=frame[x:x+h,y:y+h]
        cv2.imshow('f',facedata)
        
        cv2.imshow('face',frame)
       

        if cv2.waitKey(10) & 0xff == ord('q'):
            break
cv2.destroyAllWindows()
cap.release()





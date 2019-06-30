#!/usr/bin/python3
import cv2
# staring cmera  
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    #converting image frame  into gray scale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)
#now showing
#now we can draw pattern
 
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    cv2.circle(frame,(250,300),20,(23,67,98),2) #circle center is radius  and start point is  mid poinnt
    font=cv2.FONT_HERSHEY_SIMPLEX   # font type
    cv2.putText(frame,'OPENcv',(10,50),font,2,(0,2,55),2,cv2.LINE_AA)
    cv2.imshow('live',frame-50)

    cv2.imshow('livegray',grayimg)
    #cv2.imshow('live1',frame)
   # cv2.imshow('live2',frame)
   # cv2.imshow('live3',frame)

    if cv2.waitKey(10) & 0xff ==ord('q'):
            break           #for asci value
#cv2.destroyAllWindow('live')      for single
cv2.destroyAllWindowa() # this will distroy all winndow

cap.release() # to close camera after capure


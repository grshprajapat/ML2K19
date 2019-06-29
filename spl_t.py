#!/usr/bin/python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
#chccking version
print(cv2.__version__)
#image read
#image name ,image propert
myimg=np.zeros((512,512))
img=cv2.imread("dog-706.jpg",1)
#split
x,y,z=cv2.split(img)
#plt.imshow(img)
cv2.line(img,(0,0),(200,230),(0,0,255),3)
cv2.rectangle(img,(50,50),(200,150),(255,0,0),-6)
cv2.imshow('my',img)
#cv2.imshow('dog1',img1)
#wait for window to clos
cv2.waitKey(0) #,mili second

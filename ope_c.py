#!/usr/bin/python3
import cv2
import matplotlib.pyplot as plt
#chccking version
print(cv2.__version__)
#image read
#image name ,image property
img=cv2.imread("dog-706.jpg",1)
img1=cv2.imread("dog-706.jpg",2)
img2=cv2.imread("dog-706.jpg",-1)
#1 means in same color channel --grb or rgb
# 0 means no color 
#-1 maintain image transperancy
print(img)
#print shape
print(img.shape)
#type
print(type(img))
#to display image

#plt.imshow(img)
cv2.imshow('dog',img[0:200,0:400])
cv2.imshow('dog2',img)
#cv2.imshow('dog1',img1)
#wait for window to clos
cv2.waitKey(0) #,mili second

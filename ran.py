#!/usr/bin/python3
import numpy as np
import random
m=int(input())                #To take integer input from user
n=int(input())
y=np.random.random((m,n))     #Inserting random elements in 2d array
np.savetxt('a1.txt',y)        #Saving the array to a file
np.loadtxt('a1.txt')

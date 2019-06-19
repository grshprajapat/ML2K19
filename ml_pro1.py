#!/usr/bin/python3

import numpy as np 
  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
  
print("Enter the entries in a single line (separated by space): ") 
  
# User input of entries in a  
# single line separated by space 
entries = list(map(int, input().split())) 
  
# For printing the matrix 
matrix = np.array(entries).reshape(R, C) 
print(matrix) 
y=np.savetxt('file.npy', matrix,delimiter=' ' )
#y=np.save("file.npy", matrix)
#y.savetxt("matrix")
#y.close
print(y)

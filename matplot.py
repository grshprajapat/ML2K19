#!/usr/bin/python3
import matplotlib.pyplot as plt
x=[2,3]
x1=[4,3,8]
y1=[2,9,7]
y=[9,5]

plt.xlabel("time")
plt.ylabel("speed")
plt.plot(x,y, label="water") #it will draw an straight line
plt.plot(x1,y1,label="sand") #it will sjow label sand
plt.bar(x1,y1,label="red") # bar graph
plt.bar(x,y,label="yellow")
plt.grid(color="green")#to show  color
plt.legend() # to show label
plt.xlim(0,12)#to show min  and max number in x axis
plt.ylim(0,15) #y asis
plt.show()




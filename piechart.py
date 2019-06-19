#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import time
x=[4,7,8,9,11,5]
y=[13,23,5,7,9,3]
player=["virat","dhoni","vijay","dhawan"]
runs=[120,44,77,33]
exp=[0.1,0,0,0]
#ploting graph 
#plt.xlabel('x-axix')
#plt.ylabel('y_label')
plt.pie(runs,labels=player,explode=exp,shadow=True,autopct="%1.1f%%")

#plt.bar(player,runs,label="cricketscore")
plt.grid(color='green')
plt.show()

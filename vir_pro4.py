#!/usr/bin/pythonn3
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np



p=np.array([['snanme','smark','sage','contact','studyhr'],['A',50,18,585858585,1],['B',54,19,964885984,2],['C',98,20,555555555,5]])

with open('student.csv','w') as csvFile:
    writer=csv.writer(csvFile)
    writer.writerows(p)
csvFile.close()

df=pd.read_csv('student.csv')
sname=['A','B','C']
smark=[50,54,98]
exp=[0,0,0.1]
plt.pie(smark,labels=sname,explode=exp,autopct='%1.1f%%')
plt.show()

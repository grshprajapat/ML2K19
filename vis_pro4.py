#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('http://13.234.66.67/summer19/datasets/bank.csv')

df.head(4).plot.bar('Geography','Age')  #creating a bar pyplot
#creating a pie chart
plt.show()

data_pie=df.groupby('Geography').NumOfProducts.count()
plt.pie(np.array(data_pie),labels=('france','spain','Germany'),explode=(0.05,0.05,0.05),shadow=True,autopct='%d%%')
plt.show()
#male and female % 
df.groupby('Gender').size().plot('pie',shadow=True, label='Gender' ,autopct='%1.1f%%')
plt.show()

#creating a boxplot
df.tail(4).boxplot(column="EstimatedSalary",by='Geography')
plt.show()


df.head(4).plot.bar('CustomerId','Balance')
plt.show()
                                                              
plt.scatter(df.Exited,df.Balance)
plt.xlabel('Exited')
plt.ylabel('Balance')
plt.grid(color="red")
plt.show()

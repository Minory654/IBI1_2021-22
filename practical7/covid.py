import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("full_data(2).csv")
#This is the code that imports the .csv file works.

print(covid_data.iloc[10:20,[0,2]])
#First and Third column in row 10 to 20.

Afghanistan=[]
for i in range(7996):
    if covid_data.iloc[i,1]=="Afghanistan":
        Afghanistan.append(True)
    else:
        Afghanistan.append(False)
#The "Afghanistan" is the list for Boolen that can show all the data of Afghanistan.
#I use "for" loop to test on whether the row"s location is the Afghanistan.
print(covid_data.iloc[Afghanistan,4])
#Total cases for Afghanistan.

list1=[]
for i in range(7996):
    if covid_data.iloc[i,1]=="China":
        list1.append(True)
    else:
        list1.append(False)
China_data=covid_data.iloc[list1,]
print(China_data)
a=np.mean(China_data.loc[0:,"new_cases"])
print("This is the mean for China new_cases. It's ")
print(a)
b=np.mean(China_data.loc[0:,"new_deaths"])
print("This is the mean for China new_deaths. It's ")
print(b)
#The same method to get the data for China. And calculate the mean for
#the new cases and new deaths in China use the function of the numpy.

plt.subplot(1,2,1)
plt.boxplot(China_data.loc[0:,"new_cases"],
            whis=1.5,
            )
plt.xlabel("New cases in China_boxplot")

plt.subplot(1,2,2)
plt.boxplot(China_data.loc[0:,"new_deaths"],
            whis=1.5,
            )
plt.xlabel("New cases in China_boxplot")
plt.show()
#The boxplot for China's new cases and new deaths

plt.subplot(1,2,1)
plt.plot(China_data.loc[0:,"date"], China_data.loc[0:,"new_cases"], 'bo')
plt.xticks(China_data.loc[0::5,"date"],fontsize=4,rotation=-90,)
plt.ylabel("China new_cases")
plt.subplot(1,2,2)
plt.plot(China_data.loc[0:,"date"], China_data.loc[0:,"new_deaths"], 'r+')
plt.ylabel("China_newdeaths_red")
plt.xticks(China_data.loc[0::5,"date"],fontsize=4,rotation=-90,)
plt.show()
#The original x ticks are too crowded to be seen clearly, so I adjust the gap between
#2 ticks.
#This is the two plot of new cases and new deaths overtime in China.

#How have new cases and total cases developed over time in Spain?
#(This is the chosen question)
list2=[]
for i in range(7996):
    if covid_data.iloc[i,1]=="Spain":
        list2.append(True)
    else:
        list2.append(False)
Spain_data=covid_data.iloc[list2,]

#This list can help to get data from the whole file.Just like what I've done
#to get data of Afghanistan.

plt.subplot(1,2,1)
plt.plot(Spain_data.loc[0:,"date"], Spain_data.loc[0:,"new_cases"], 'bo')
plt.xticks(Spain_data.loc[0::5,"date"],fontsize=4,rotation=-90,)
plt.ylabel("Spain new_cases")
plt.subplot(1,2,2)
plt.plot(Spain_data.loc[0:,"date"], Spain_data.loc[0:,"total_cases"], 'r+')
plt.ylabel("Spain_totalcases_red")
plt.xticks(Spain_data.loc[0::5,"date"],fontsize=4,rotation=-90,)
plt.show()
#This is the data of the Spain about new cases and total deaths.
import numpy as np
import matplotlib.pyplot as plt
paternal_age=[30,35,40,45,50,55,60,65,70,75]
#This is for creating a list of paternal age.

chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#This is for creating a list of or the relative risk of having heart diseases in child.

age_risk={}
#This is the dictionary.

for i in range(10):
    age_risk[paternal_age[i]]=chd[i]
#This loop gives each value of the dictionary.

print(age_risk)
#1.This is the output of the dictionary that the practical sheet asked for.

newage=30                  #2.This is the variable that can modify each time
print(age_risk[newage])    #This gives the value in the dictionary.(The risk of having illness.)

#3. This is the plot the Return asked for.
plt.scatter(paternal_age,chd,)
plt.xlabel("paternal_age")
plt.ylabel("chd")
plt.show()




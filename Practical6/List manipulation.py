import numpy as np
import matplotlib.pyplot as plt

#pseudocode:1.give the list an order. 2.Calculate the average through FOR loop. 3.Draw the box plot.

marks=[45,36,86,57,53,92,65,45]
#This is the list given by the practical.
marks.sort()
#This gives the list an order from low to gigh
print(marks)
#This is the 1st Return result. Show the list

avg=0.0
total=0
#This is used to calculate the score Rob gets.
for i in marks:
    avg=avg+i/len(marks)
#Calculate the average score(The score that Rob gets.)

if avg >=60:
    print("Rob got" +f"{avg}"+" . He's passed")
else:
    print("Rob got " +f"{avg}"+" . He's failed")
#f"" can transfer float to chr.
# This is the 3rd result the Return asked.

plt.boxplot(marks,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False,
            )
plt.show()
#This is the 2nd result the Return asked. I show the bosplot of the data.

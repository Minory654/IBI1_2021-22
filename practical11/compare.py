import re

import pandas
import pandas as pd
data = pd.read_excel('BLOSUM.xlsx',index_col=0)
data.to_csv('BLOSUM.csv',encoding='utf-8')
new=pandas.read_csv("BLOSUM.csv")
print(new.iloc[1,0])

def grade(a,b):
    for i in range(23):
        if a == new.iloc[i,0]:
            for m in range(23):
                if b == new.iloc[m,0]:
                    return new.iloc[i,m+1]


a=open("DLX5_human.fa",)
b=open("DLX5_mouse.fa",)
c=open("RandomSeq.fa",)

hum=a.read()
mou=b.read()
ran=c.read()

hum=re.sub(r"\n","",hum)+"1"
mou=re.sub(r"\n","",mou)+"1"
ran=re.sub(r"\n","",ran)+"1"

hum_=re.findall(r"(MTGVF.+?)1",hum)
mou_=re.findall(r"(MTGVF.+?)1",mou)
ran_=re.findall(r"(GDY.+?)1",ran)

hum_l=list(hum_[0])
mou_l=list(mou_[0])
ran_l=list(ran_[0])
hum_mou=0
hum_ran=0
ran_mou=0
for i in range(len(hum_l)):
    hum_mou=hum_mou+grade(hum_l[i],mou_l[i])
for i in range(len(hum_l)):
    hum_ran=hum_ran+grade(hum_l[i],ran_l[i])
for i in range(len(mou_l)):
    ran_mou=ran_mou+grade(ran_l[i],mou_l[i])
print("The rule for grading is +1 for each same amino acid and 0 for each different amino acid at the same site.")
print("The similarity score between human and mouse sequence is ",hum_mou)

print("The similarity score between human and random sequence is ",hum_ran)

print("The similarity score between mouse and random sequence is ",ran_mou)
n1=0
n2=0
n3=0
for i in range(len(hum_l)):
    if hum_l[i]==mou_l[i]:
        n1+=1
for i in range(len(hum_l)):
    if hum_l[i]==ran_l[i]:
        n2+=1
for i in range(len(mou_l)):
    if ran_l[i]==mou_l[i]:
        n3+=1
print("The percentage of same amino acid between human and mouse is ",n1/len(hum_l))
print("The percentage of same amino acid between human and random sequence is ",n2/len(hum_l))
print("The percentage of same amino acid between mouse and random sequence is ",n3/len(hum_l))

import re
def grade(a,b):
    if a==b:
        return 1
    else:
        return 0
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

print("The percentage of same amino acid between human and mouse is ",hum_mou/len(hum_l))
print("The percentage of same amino acid between human and random sequence is ",hum_ran/len(hum_l))
print("The percentage of same amino acid between mouse and random sequence is ",ran_mou/len(hum_l))
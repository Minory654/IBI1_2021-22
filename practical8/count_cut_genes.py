import re
print("Input the filename for the outcome of adding EcoRI to sequence: (Remember adding .fa behind the name)")
h=input()                       #give name of the output format
new=open(h,"w")                 #create output file

b=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")          #import given fasta file
har=b.read()
clear=re.sub(r"\n","",har)      #clear "\n" of the file
z = re.findall(r'[AGCT]{10,}',clear) #create list "z" that encodes all the raw sequence
length=[]                            #create a list of length of the sequence

n=[]                        #The order of sequence in the original file
y=[]
for i in range(len(z)):
    if z[i].find("GAATTC")>=0:
        n.append(i)
        length.append(len(z[i]))     #search sequence that can be cut by EcoRI
        y.append(z[i])

names=re.findall(r"(>.+?) ",clear)


n=[]                            #The fragments created by EcoRI
a=0                             #The number of fragments





for i in range(len(z)):
    a=z[i].find("GAATTC",)
    n.append(a+2)          #number of fragments
for i in range(len(z)):
    new.write(names[i]+"    ")
    new.write("fragments'number after cutting by EcoRI: ")
    new.write(str(n[i])+"\n")
    new.write(z[i]+"\n")
new.close()




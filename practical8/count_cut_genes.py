import re
b=open("cut_genes.fa")          #import file containing sequence that can be cut by EcoRI

print("Input the filename for the outcome of adding EcoRI to sequence:")
h=input()                       #give name of the output format
new=open(h,"w")                 #create output file

har=b.read()
clear=re.sub(r"\n","",har)      #clear "\n" of the file

n=[]                            #The fragments created by EcoRI
a=0                             #The number of fragments

z = re.findall(r'[AGCT]{10,}',clear) #create list "z" that encodes all the raw sequence

names=re.findall(r"(>.+?) ",clear)
for i in range(len(z)):
    a=z[i].find("GAATTC",)
    n.append(a+2)
for i in range(len(z)):
    new.write(names[i]+"    ")
    new.write("fragments'number after cutting by EcoRI: ")
    new.write(str(n[i])+"\n")
    new.write(z[i]+"\n")
new.close()




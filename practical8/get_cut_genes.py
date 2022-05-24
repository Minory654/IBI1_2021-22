import re
b=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")          #import given fasta file
new=open("cut_genes.fa","w")                                    #create output file

har=b.read()
clear=re.sub(r"\n","",har)                                      #clear "\n" of the file
#Now clear is the string without\n of the original file


n=[]                        #The order of sequence in the original file

y=[]

z = re.findall(r'[AGCT]{10,}',clear) #create list "z" that encodes all the raw sequence
length=[]                            #create a list of length of the sequence

for i in range(len(z)):
    if z[i].find("GAATTC")>=0:
        n.append(i)
        length.append(len(z[i]))     #search sequence that can be cut by EcoRI
        y.append(z[i])






names=[]
g=re.findall(r"gene:(.+?) gene_biotyp",clear)#gene names of sequence
for i in n:
    names.append(g[i])


for i in range(len(names)):
    new.write("> ")
    new.write(names[i]+" ")
    k=str(length[i])
    new.write(k)
    new.write("\n")
    new.write(y[i]+"\n")
new.close()


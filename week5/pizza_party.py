#pseudocode:
#cut
# Calculate the number of parts that parts made
#increase the cuts
#until the number of parts is enough
i=0#The number of cuts
p=1#The pieces of pizza
while p<64:
    i=i+1#increase the cuts
    p=(i*i+i+2)/2#caculate the result
    if p<64:
        print(str(i) + " cuts will get at most "+str(p) +" parts of pizza, and that's not enough")
    else:
        print(str(i) + " cuts will get at most " + str(p) + " parts of pizza, and that's enough")
print("The number of cuts needed is " + str(i))

seq ="ATGCAATCGACTACGATCAATCGAGGGCC"
cuts=seq.find("GAATTC") #Import sequence and calculate number of cuts.
print("When the DNA is added with EcoRI")
if cuts >=0:            # Make jugement on number of cuts.
    print("The number of cuts are",cuts+1,".So there are",cuts+2, "fragments.")
else:
    print("No cuts. The number of fragment is 1.")

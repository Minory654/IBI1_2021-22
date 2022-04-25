import re
def DNA(seq):
	seq_list = list(seq)
	A = 0
	G = 0
	C = 0
	T = 0
	for i in range(len(seq_list)):
		if seq_list[i] == "a":
			seq_list[i] = "A"
		if seq_list[i] == "g":
			seq_list[i] = "G"
		if seq_list[i] == "c":
			seq_list[i] = "C"
		if seq_list[i] == "t":
			seq_list[i] = "T"
	for i in range(len(seq_list)):
		if seq_list[i] == "A":
			A = A + 1
		if seq_list[i] == "G":
			G = G + 1
		if seq_list[i] == "C":
			C = C + 1
		if seq_list[i] == "T":
			T = T + 1
	total = A + G + C + T
	print("A:", A / total, " G:", G / total, " C:", C / total, " T:", T / total, )
	return(A/total,G/total,C/total,T/total)
print("Input the sequence, and the program give the percentage of each nucleotides")

seq=input()
#input the code needed.
#FOR EXAMPLE here we choose "AAGAGAGAGCTCTCTAGAGCTTCactgactg"

DNA(seq)
#the answer is
#Input the sequence, and the program give the percentage of each nucleotides
#AAGAGAGAGCTCTCTAGAGCTTCactgactg
#A: 0.2903225806451613  G: 0.25806451612903225  C: 0.22580645161290322  T: 0.22580645161290322
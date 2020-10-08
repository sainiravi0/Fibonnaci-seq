#program to print fibonnaci sequence


seq = [0, 1]

def main(n):
	for value in range(0,n):
		seq.append(seq[value] + seq[value + 1])
	print(seq)
		
		
main(12)
print(seq[4])
	

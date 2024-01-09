seq = input()
# seq=  "ATTCGGGGGA"

i = j = count = 0
while j < len(seq):
	if seq[i] != seq[j]:
		count = max(count, j - i)
		i = j
	j += 1
	
if i < j:
	count = max(count, j - i)
print(count)
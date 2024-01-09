from itertools import permutations

seq = input()
# seq = "aabac"

possible = sorted(set(map(lambda x: "".join(x), permutations(seq))))

print(len(possible))
for i in possible:
	print(i)
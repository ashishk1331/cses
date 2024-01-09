seq = input()
# seq = "ABZ"

dmap = {}
for i in seq:
	if i in dmap:
		dmap[i] += 1
	else:
		dmap[i] = 1

res = ""
middle = ""
double = 0
for char, times in sorted(dmap.items(), key=lambda x: x[1]):
	if times%2:
		middle = char
		double += 1

	res = char*int(times/2) + res

if double > 1:
	print("NO SOLUTION")
else:
	print(res + middle + res[::-1])
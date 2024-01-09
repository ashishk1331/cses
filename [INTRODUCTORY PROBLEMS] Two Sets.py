n = int(input())

mus = n*(n+1)//2

if mus%2:
	print("NO")
else:
	print("YES")
	a, b = [], []
	sum_a, sum_b = 0, 0
	for i in range(n, 0, -1):
		if sum_a < sum_b:
			a.append(i)
			sum_a += i
		else:
			b.append(i)
			sum_b += i
	print(len(a)," ".join(map(str, a)), sep="\n")
	print(len(b)," ".join(map(str, b)), sep="\n")
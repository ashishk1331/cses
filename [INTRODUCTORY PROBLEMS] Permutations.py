n = int(input())
# n= 5

if n == 1:
	print("1")
elif n < 4:
	print('NO SOLUTION')
else:
	per = [x for x in range(2, n + 1, 2)]
	per.extend([x for x in range(1, n + 1, 2)])
	print(" ".join(map(str, per)))
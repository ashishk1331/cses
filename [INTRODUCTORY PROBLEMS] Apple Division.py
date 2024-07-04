n = int(input())
arr = list(map(int, input().split()))
# n, arr = 20, [314836307, 815098885, 922742346, 53006071, 757943472, 481505203, 354207278, 175676232, 335088325, 921705085, 231986392, 619406418, 170606376, 498080884, 415616625, 40905556, 110076295, 642911923, 932231564, 381545587]
# masks = []

res = float("inf")

for num in range(2**n):
	a, b = 0, 0
	for j in range(n):
		if num & (1 << j):
			a += arr[j]
		else:
			b += arr[j]
	res = min(res, abs(a - b))
print(res)